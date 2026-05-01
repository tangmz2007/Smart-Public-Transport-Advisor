import heapq
import math
from metro_data import DEFAULT_TRANSFER_TIME, CARBON_CONFIG
from metro_input import normalize_text


class RouteState:
    """Represents a partial route during search (used as a node in priority queue)."""

    def __init__(self, priority_key, total_time, fare_units, total_cost,
                 transfer_count, walk_time, crowding_burden, in_vehicle_time,
                 high_crowding_minutes, stair_burden, current_station,
                 current_line, current_direction_key, path_stations,
                 path_lines, path_directions, path_segment_ids, current_clock):
        self.priority_key = priority_key
        self.total_time = total_time
        self.fare_units = fare_units  # Kept for backward compatibility in object, though unused for pricing now
        self.total_cost = total_cost
        self.transfer_count = transfer_count
        self.walk_time = walk_time
        self.crowding_burden = crowding_burden
        self.in_vehicle_time = in_vehicle_time
        self.high_crowding_minutes = high_crowding_minutes
        self.stair_burden = stair_burden
        self.current_station = current_station
        self.current_line = current_line
        self.current_direction_key = current_direction_key
        self.path_stations = path_stations
        self.path_lines = path_lines
        self.path_directions = path_directions
        self.path_segment_ids = path_segment_ids
        self.current_clock = current_clock


class RouteResult:
    """Holds the final information of a completed route."""

    def __init__(self, total_time, total_cost, fare_units, transfer_count,
                 walk_time, crowding_burden, avg_crowding, in_vehicle_time,
                 high_crowding_minutes, stair_burden, arrival_time,
                 stations, lines, directions, segment_ids, entry_name,
                 entry_walk, entry_msg, exit_name, exit_walk, exit_reason,
                 instructions, carbon_saved_kg=0.0, reason=""):
        self.total_time = total_time
        self.total_cost = total_cost
        self.fare_units = fare_units
        self.transfer_count = transfer_count
        self.walk_time = walk_time
        self.crowding_burden = crowding_burden
        self.avg_crowding = avg_crowding
        self.in_vehicle_time = in_vehicle_time
        self.high_crowding_minutes = high_crowding_minutes
        self.stair_burden = stair_burden
        self.arrival_time = arrival_time
        self.stations = stations
        self.lines = lines
        self.directions = directions
        self.segment_ids = segment_ids
        self.entry_name = entry_name
        self.entry_walk = entry_walk
        self.entry_msg = entry_msg
        self.exit_name = exit_name
        self.exit_walk = exit_walk
        self.exit_reason = exit_reason
        self.instructions = instructions
        self.carbon_saved_kg = carbon_saved_kg
        self.reason = reason


def time_to_minutes(t_str):
    """Converts a time string 'HH:MM' to total minutes since midnight."""
    h, m = map(int, t_str.split(":"))
    return h * 60 + m


def minutes_to_time(mins):
    """Converts total minutes back to 'HH:MM' format (24-hour clock)."""
    mins %= 24 * 60
    return f"{mins // 60:02d}:{mins % 60:02d}"


def get_period_value(periods, current_time):
    """Returns the value for the period that contains current_time."""
    for start, end, value in periods:
        s = time_to_minutes(start)
        e = time_to_minutes(end)
        if s <= current_time < e:
            return value
    if periods:
        last_end = time_to_minutes(periods[-1][1])
        if current_time == last_end:
            return periods[-1][2]
    return None


def get_direction_key(line_info, current_station, next_station):
    """Determines whether travel is in 'forward' or 'backward' direction."""
    i = line_info["index_map"][current_station]
    j = line_info["index_map"][next_station]
    if j > i:
        return "forward", line_info["directions"]["forward"]["label"]
    return "backward", line_info["directions"]["backward"]["label"]


def get_next_departure_time(line_info, direction_key, ready_time):
    """Returns the next departure time considering headways and disruptions."""
    direction = line_info["directions"][direction_key]
    first_train = time_to_minutes(direction["first_train"])
    last_train = time_to_minutes(direction["last_train"])

    if ready_time > last_train:
        return None

    search_time = max(ready_time, first_train)

    for start, end, headway in direction["headway"]:
        s = max(time_to_minutes(start), first_train)
        e = min(time_to_minutes(end), last_train)
        if e < s or search_time > e:
            continue

        candidate_base = max(search_time, s)
        if candidate_base <= s:
            dep = s
        else:
            dep = s + math.ceil((candidate_base - s) / headway) * headway

        while dep <= e and dep <= last_train:
            extra_delay = 0
            suspended = False
            for start_dis, end_dis, action, value in direction.get("disruption_windows", []):
                s_dis = time_to_minutes(start_dis)
                e_dis = time_to_minutes(end_dis)
                if s_dis <= dep < e_dis:
                    if action == "suspend":
                        suspended = True
                        break
                    if action == "delay":
                        extra_delay += int(value or 0)

            if not suspended:
                return dep + extra_delay
            dep += headway
    return None


def get_crowding(line_info, direction_key, current_time):
    """Returns the crowding level for the given line, direction, and time."""
    direction = line_info["directions"][direction_key]
    value = get_period_value(direction["crowding"], current_time)
    return value if value is not None else 3


def choose_entry(station_name, station_info, preferred_entry="", preferred_line="", accessibility=False):
    """Selects the best entrance for a given station based on user preferences."""
    if station_name not in station_info or "entries" not in station_info[station_name]:
        return "Default Entrance", 0, "No entry walking data is available for this station; 0 minutes assumed."

    entries_raw = station_info[station_name]["entries"]
    entries = {}
    for name, value in entries_raw.items():
        if isinstance(value, dict):
            entries[name] = {"walk": int(value.get("walk", 0)), "line_bias": value.get("line_bias", {})}
        else:
            entries[name] = {"walk": int(value), "line_bias": {}}

    if preferred_entry and preferred_entry in entries:
        walk = entries[preferred_entry]["walk"]
        return preferred_entry, walk, f"Using your specified entrance {preferred_entry}; about {walk} minutes of walking."

    def entry_score(entry_name):
        info = entries[entry_name]
        bias = info["line_bias"].get(preferred_line, 0) if preferred_line else 0
        return (info["walk"] + bias, info["walk"], entry_name)

    best = min(entries, key=entry_score)
    walk = entries[best]["walk"]
    if preferred_line and entries[best]["line_bias"].get(preferred_line, 0) == 0:
        msg = f"Defaulted to entrance {best}, which is closer to the {preferred_line} platform and has better overall walking time; about {walk} minutes."
    else:
        msg = f"Defaulted to entrance {best} with the best overall walking time; about {walk} minutes."
    return best, walk, msg


def recommend_exit(station_name, station_info, desired_landmark="", accessibility=False, prefer_walk=False):
    """Recommends an exit based on desired landmark (fuzzy matched) or general criteria."""
    if station_name not in station_info or "exits" not in station_info[station_name]:
        return "Default Exit", 0, "No exit walking data is available for this station."

    exits_raw = station_info[station_name]["exits"]
    exits = {}
    for exit_name, landmarks in exits_raw.items():
        items = []
        for item in landmarks:
            if isinstance(item, dict):
                items.append({
                    "landmark": item["landmark"],
                    "walk": int(item["walk"]),
                    "elevator": bool(item.get("elevator", False)),
                    "stairs": int(item.get("stairs", 0)),
                })
            else:
                landmark, walk = item
                items.append({"landmark": landmark, "walk": int(walk), "elevator": False, "stairs": 0})
        exits[exit_name] = items

    target = normalize_text(desired_landmark)
    if target:
        def landmark_match_score(query, candidate):
            q = normalize_text(query)
            c = normalize_text(candidate)
            if q == c:
                return 100
            if q in c or c in q:
                return 70
            common = sum(1 for ch in set(q) if ch in c)
            return common * 5

        best_candidates = []
        for exit_name, items in exits.items():
            for item in items:
                match = landmark_match_score(target, item["landmark"])
                if match > 0:
                    score = (
                        -match,
                        0 if (not accessibility or item["elevator"]) else 1,
                        item["stairs"],
                        item["walk"],
                    )
                    best_candidates.append((score, exit_name, item))

        if best_candidates:
            best_candidates.sort()
            _, best_exit, best_item = best_candidates[0]
            msg = f'Recommended exit: {best_exit}. Walking time to "{best_item["landmark"]}" is about {best_item["walk"]} minutes.'
            if accessibility and best_item["elevator"]:
                msg += " This exit has elevator information and is better for avoiding stairs."
            return best_exit, best_item["walk"], msg

    best_exit = None
    best_score = None
    best_avg_walk = 0
    for exit_name, items in exits.items():
        avg_walk = sum(i["walk"] for i in items) / len(items)
        elevator_ratio = sum(1 for i in items if i["elevator"]) / len(items)
        avg_stairs = sum(i["stairs"] for i in items) / len(items)
        if accessibility:
            score = (-elevator_ratio, avg_stairs, avg_walk)
        elif prefer_walk:
            score = (avg_walk, avg_stairs, -elevator_ratio)
        else:
            score = (avg_walk, -elevator_ratio, avg_stairs)
        if best_score is None or score < best_score:
            best_score = score
            best_exit = exit_name
            best_avg_walk = avg_walk

    walk = round(best_avg_walk) if best_exit else 0
    msg = f"Default recommended exit: {best_exit}. Estimated average walking time around that exit is about {walk} minutes."
    if accessibility:
        msg += " Elevator access and fewer stairs were prioritized."
    return best_exit, walk, msg


def get_transfer_time(transfer_times, station, from_line, to_line):
    """Returns the walking time (in minutes) for transferring between two lines."""
    return transfer_times.get((station, from_line, to_line), DEFAULT_TRANSFER_TIME)


def build_graph(lines):
    """Constructs an adjacency-list graph from metro line definitions."""
    graph = {}
    for line_name, info in lines.items():
        stations = info["stations"]
        run_times = info["run_times"]
        fare = info["fare_per_segment"]
        for station in stations:
            graph.setdefault(station, [])
        for i in range(len(stations) - 1):
            a, b = stations[i], stations[i + 1]
            t = run_times[i]
            graph[a].append((b, line_name, t, fare, f"{line_name}:{a}->{b}"))
            graph[b].append((a, line_name, t, fare, f"{line_name}:{b}->{a}"))
    return graph


def calculate_fare_by_time(t_minutes):
    """
    New pricing mechanism: Linear fitting pricing P = a * T + b based on total in-vehicle time (T).
    Adjusted in segments referring to actual MTR fare standards:
    """
    if t_minutes <= 0:
        return 0.0

    # T < 12 minutes: Short distance, higher base fare
    if t_minutes < 12:
        a, b = 0.45, 1.0
    # 12 <= T <= 25 minutes: Medium distance, unit price decreases
    elif t_minutes <= 25:
        a, b = 0.65, -1.4  # Slightly lowered 'b' to ensure smooth transition around 12 mins
    # T > 25 minutes: Long distance, lowest unit price
    else:
        a, b = 0.30, 7.35  # Adjusted 'b' to reflect fixed costs for cross-territory routes

    fare = a * t_minutes + b
    # Simulating MTR fare unit precision (usually rounded to 1 decimal place, e.g., HK$0.5 or 0.1)
    return round(fare, 1)


def compute_priority(preference, total_time, total_cost, transfer_count, walk_time,
                     crowding_burden, in_vehicle_time, high_crowding_minutes, stair_burden):
    """Calculates the priority tuple for the A* search queue based on user preference."""
    avg_crowding = crowding_burden / max(1, in_vehicle_time)

    if preference == "time":
        return (total_time, total_cost, transfer_count, walk_time, round(avg_crowding, 4), stair_burden)
    if preference == "cost":
        return (total_cost, total_time, transfer_count, walk_time, round(avg_crowding, 4), stair_burden)
    if preference == "transfer":
        return (transfer_count, total_time, total_cost, walk_time, round(avg_crowding, 4), stair_burden)
    if preference == "walk":
        return (walk_time, transfer_count, total_time, total_cost, round(avg_crowding, 4), stair_burden)
    if preference == "accessible":
        return (stair_burden, walk_time, transfer_count, total_time, total_cost, round(avg_crowding, 4))
    if preference == "comfort":
        comfort_score = round(crowding_burden + transfer_count * 8 + walk_time * 1.2 + high_crowding_minutes * 1.5, 2)
        return (comfort_score, round(avg_crowding, 4), transfer_count, walk_time, total_time, total_cost, stair_burden)

    # Balanced preference: weighted sum
    score = (
            total_time * 0.60
            + total_cost * 1.20
            + transfer_count * 4.00
            + walk_time * 0.80
            + crowding_burden * 0.35
            + high_crowding_minutes * 0.60
            + stair_burden * 0.80
    )
    return (round(score, 2), total_time, total_cost, transfer_count, walk_time)


def route_signature(lines_used, stations_used, directions_used):
    """Generates a unique signature for a route to avoid duplicate paths."""
    if not lines_used:
        return ("SAME",)
    compressed = []
    seg_start = 0
    for i in range(1, len(lines_used) + 1):
        if i == len(lines_used) or lines_used[i] != lines_used[seg_start] or directions_used[i] != directions_used[
            seg_start]:
            compressed.append(
                (lines_used[seg_start], directions_used[seg_start], stations_used[seg_start], stations_used[i]))
            seg_start = i
    return tuple(compressed)


def label_dominates(a, b):
    """
    Optimized Pareto dominance check.
    Checks if route 'a' dominates route 'b'.
    Domination means 'a' is not worse than 'b' in ALL metrics,
    AND strictly better than 'b' in at least ONE metric.
    """
    has_strict_improvement = False
    for val_a, val_b in zip(a, b):
        # If 'a' is worse in any metric, it cannot dominate 'b'
        if val_a > val_b:
            return False
        # Record if 'a' is strictly better in at least one metric
        if val_a < val_b:
            has_strict_improvement = True

    return has_strict_improvement


def build_instructions(stations, lines_used, directions_used,
                       entry_name, entry_walk, exit_name, exit_walk, exit_reason):
    """Constructs a human-readable list of instructions for a complete route."""
    instructions = []
    if entry_name:
        instructions.append(
            f"Enter the station via {entry_name} at {stations[0]}. Estimated walk to the platform: {entry_walk} minutes."
        )
    if not lines_used:
        instructions.append("The origin and destination are the same.")
        return instructions

    seg_start = 0
    for i in range(1, len(lines_used) + 1):
        if i == len(lines_used) or lines_used[i] != lines_used[seg_start] or directions_used[i] != directions_used[
            seg_start]:
            from_station = stations[seg_start]
            to_station = stations[i]
            line = lines_used[seg_start]
            direction = directions_used[seg_start]
            if seg_start == 0:
                instructions.append(f"Take {line} ({direction}) from {from_station} to {to_station}.")
            else:
                instructions.append(
                    f"Transfer at {from_station} to {line} ({direction}), then continue to {to_station}.")
            seg_start = i
    instructions.append(
        f"After arriving at {stations[-1]}, leave via {exit_name}. Estimated walk after exit: {exit_walk} minutes. {exit_reason}"
    )
    return instructions


def estimate_carbon_saved(in_vehicle_time, config=CARBON_CONFIG):
    """Estimates CO2 saved (in kg) by taking the metro instead of a car."""
    estimated_distance_km = in_vehicle_time / 60 * config["metro_avg_kmh"]
    metro_emission = estimated_distance_km * config["metro_kg_per_passenger_km"]
    car_emission = estimated_distance_km * config["car_kg_per_passenger_km"]
    saved = max(0.0, car_emission - metro_emission)
    return round(saved, 3), round(estimated_distance_km, 2)


def find_routes(graph, lines, transfer_times, station_info, start, target, departure_time, k=3,
                preference="time", max_budget=None, preferred_entry="",
                desired_landmark="", schedule_mode="accurate", accessibility=False,
                max_results_multiplier=8):
    """
    Main routing algorithm using a priority-queue based search (similar to A* / Dijkstra
    but with multiple weighted objectives). Returns up to 'k' best routes according to
    the user's preference.
    """
    # Determine entry/exit recommendations upfront
    possible_lines = sorted({line_name for _, line_name, _, _, _ in graph.get(start, [])})
    preferred_line_for_entry = possible_lines[0] if possible_lines else ""
    entry_name, entry_walk, entry_msg = choose_entry(
        start, station_info, preferred_entry, preferred_line_for_entry, accessibility
    )
    exit_name, exit_walk, exit_reason = recommend_exit(
        target, station_info, desired_landmark, accessibility, preference == "walk"
    )

    # Initial state (after walking to platform)
    start_clock = time_to_minutes(departure_time) + entry_walk
    start_priority = compute_priority(preference, entry_walk, 0, 0, entry_walk, 0, 0, 0, 0)

    pq = []
    counter = 0
    start_state = RouteState(
        priority_key=start_priority, total_time=entry_walk, fare_units=0, total_cost=0,
        transfer_count=0, walk_time=entry_walk, crowding_burden=0, in_vehicle_time=0,
        high_crowding_minutes=0, stair_burden=0, current_station=start,
        current_line=None, current_direction_key=None, path_stations=[start],
        path_lines=[], path_directions=[], path_segment_ids=[], current_clock=start_clock,
    )
    heapq.heappush(pq, (start_priority, counter, start_state))

    results = []
    seen_signatures = set()
    best_labels = {}
    max_results = max(k * max_results_multiplier, k)

    while pq and len(results) < max_results:
        _, _, state = heapq.heappop(pq)

        # Destination reached?
        if state.current_station == target:
            final_total_time = state.total_time + exit_walk
            final_walk_time = state.walk_time + exit_walk
            final_arrival_clock = state.current_clock + exit_walk
            avg_crowding = round(state.crowding_burden / max(1, state.in_vehicle_time), 2)

            sig = route_signature(state.path_lines, state.path_stations, state.path_directions)
            if sig in seen_signatures:
                continue
            seen_signatures.add(sig)

            instructions = build_instructions(
                state.path_stations, state.path_lines, state.path_directions,
                entry_name, entry_walk, exit_name, exit_walk, exit_reason
            )
            carbon_saved_kg, _ = estimate_carbon_saved(state.in_vehicle_time)
            route = RouteResult(
                total_time=final_total_time, total_cost=state.total_cost,
                fare_units=state.fare_units, transfer_count=state.transfer_count,
                walk_time=final_walk_time, crowding_burden=state.crowding_burden,
                avg_crowding=avg_crowding, in_vehicle_time=state.in_vehicle_time,
                high_crowding_minutes=state.high_crowding_minutes, stair_burden=state.stair_burden,
                arrival_time=minutes_to_time(int(final_arrival_clock)), stations=state.path_stations,
                lines=state.path_lines, directions=state.path_directions,
                segment_ids=state.path_segment_ids, entry_name=entry_name,
                entry_walk=entry_walk, entry_msg=entry_msg, exit_name=exit_name,
                exit_walk=exit_walk, exit_reason=exit_reason, instructions=instructions,
                carbon_saved_kg=carbon_saved_kg,
            )
            results.append(route)
            continue

        # Prune using Pareto frontier for this (station, line, direction)
        label_key = (state.current_station, state.current_line, state.current_direction_key)
        current_label = (
            state.total_time, state.total_cost,  # Cost replaces fare units in metric comparison
            state.transfer_count, state.walk_time, state.crowding_burden, state.stair_burden,
        )
        existing = best_labels.get(label_key, [])
        if any(label_dominates(old, current_label) for old in existing):
            continue

        existing = [old for old in existing if not label_dominates(current_label, old)]
        existing.append(current_label)
        best_labels[label_key] = existing

        # Explore neighbors
        for next_station, line_name, run_time, fare_units, seg_id in graph.get(state.current_station, []):
            line_info = lines[line_name]
            direction_key, direction_label = get_direction_key(line_info, state.current_station, next_station)

            extra_walk = 0
            extra_transfer = 0
            extra_stairs = 0

            # Calculate transfer penalties if switching lines
            if state.current_line is not None and state.current_line != line_name:
                extra_transfer = get_transfer_time(transfer_times, state.current_station, state.current_line, line_name)
                extra_walk += extra_transfer
                extra_stairs += 1

            ready_time = state.current_clock + extra_walk

            # Handle train schedules and delays
            if schedule_mode == "accurate":
                departure_clock = get_next_departure_time(line_info, direction_key, int(ready_time))
                if departure_clock is None:
                    continue
            else:
                direction = line_info["directions"][direction_key]
                headway = get_period_value(direction["headway"], int(ready_time))
                departure_clock = ready_time + (headway / 2 if headway else 0)

            waiting_time = max(0, departure_clock - ready_time)
            crowding = get_crowding(line_info, direction_key, int(departure_clock))
            high_crowding_minutes = run_time if crowding >= 4 else 0

            # New pricing calculation
            next_in_vehicle_time = state.in_vehicle_time + run_time
            next_total_cost = calculate_fare_by_time(next_in_vehicle_time)

            # kill routes that exceed user's maximum budget
            if max_budget is not None and next_total_cost > max_budget:
                continue

            # Accumulate next state variables
            next_total_time = state.total_time + extra_walk + waiting_time + run_time
            next_walk_time = state.walk_time + extra_walk
            next_crowding_burden = state.crowding_burden + crowding * run_time
            next_high_crowding_minutes = state.high_crowding_minutes + high_crowding_minutes
            next_stair_burden = state.stair_burden + extra_stairs
            next_clock = departure_clock + run_time
            next_transfer_count = state.transfer_count + (
                1 if state.current_line is not None and state.current_line != line_name else 0)
            next_fare_units = state.fare_units + fare_units  # Kept structurally but not utilized for cost

            next_priority = compute_priority(
                preference, next_total_time, next_total_cost, next_transfer_count,
                next_walk_time, next_crowding_burden, next_in_vehicle_time,
                next_high_crowding_minutes, next_stair_burden,
            )

            counter += 1
            next_state = RouteState(
                priority_key=next_priority, total_time=next_total_time, fare_units=next_fare_units,
                total_cost=next_total_cost, transfer_count=next_transfer_count, walk_time=next_walk_time,
                crowding_burden=next_crowding_burden, in_vehicle_time=next_in_vehicle_time,
                high_crowding_minutes=next_high_crowding_minutes, stair_burden=next_stair_burden,
                current_station=next_station, current_line=line_name, current_direction_key=direction_key,
                path_stations=state.path_stations + [next_station], path_lines=state.path_lines + [line_name],
                path_directions=state.path_directions + [direction_label],
                path_segment_ids=state.path_segment_ids + [seg_id],
                current_clock=next_clock,
            )
            heapq.heappush(pq, (next_priority, counter, next_state))

    # Sort final results according to the user's preference
    results.sort(
        key=lambda r: compute_priority(
            preference, r.total_time, r.total_cost, r.transfer_count, r.walk_time,
            r.crowding_burden, r.in_vehicle_time, r.high_crowding_minutes, r.stair_burden
        )
    )
    return results[:k]