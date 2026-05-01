import ast
import difflib

def parse_txt_sections_from_text(text):
    """
    Parses a custom text format where sections are marked by [SectionName] headers.
    Returns a dictionary mapping section names to their content strings.
    """
    sections = {}
    current_name = None
    buffer = []

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()

        # Ignore initial comments before any section starts
        if stripped.startswith("#") and current_name is None:
            continue

        # Detect a new section header: [section_name]
        if stripped.startswith("[") and stripped.endswith("]"):
            if current_name is not None:
                sections[current_name] = "\n".join(buffer).strip()
            current_name = stripped[1:-1].strip()
            buffer = []
            continue

        # Accumulate lines belonging to the current section
        if current_name is not None:
            buffer.append(line)

    # Save the last section if present
    if current_name is not None:
        sections[current_name] = "\n".join(buffer).strip()

    return sections

def load_data_from_text(text):
    """
    Loads metro network data from the provided text.
    Sections expected: METRO_LINES, TRANSFER_TIMES, STATION_INFO.
    Uses ast.literal_eval for safe parsing of Python literals.
    Returns (metro_lines, transfer_times, station_info).
    """
    sections = parse_txt_sections_from_text(text)
    metro_lines = ast.literal_eval(sections["METRO_LINES"])
    transfer_time_list = ast.literal_eval(sections["TRANSFER_TIMES"])
    station_info = ast.literal_eval(sections["STATION_INFO"])

    # Convert transfer times list to a dictionary keyed by (station, from_line, to_line)
    transfer_times = {
        (station, from_line, to_line): minutes
        for station, from_line, to_line, minutes in transfer_time_list
    }

    # Build an index map (station name -> position in line) for each line
    for line_name, info in metro_lines.items():
        info["index_map"] = {station: i for i, station in enumerate(info["stations"])}

    return metro_lines, transfer_times, station_info

def normalize_text(text):
    """
    Normalizes a string by lowercasing, removing spaces, and stripping.
    Used for fuzzy matching of station names and landmarks.
    """
    return "".join(str(text).strip().lower().split())

def build_search_index(graph, station_info):
    """
    Builds data structures for fast station/landmark lookup and fuzzy search.
    """
    station_names = sorted(graph.keys())
    landmark_to_station = {}

    for station, info in station_info.items():
        for landmarks in info.get("exits", {}).values():
            for item in landmarks:
                landmark = item["landmark"] if isinstance(item, dict) else item[0]
                landmark_to_station[landmark] = station

    return {
        "stations": station_names,
        "station_norm_map": {normalize_text(name): name for name in station_names},
        "landmark_map": landmark_to_station,
        "landmark_norm_map": {normalize_text(name): station for name, station in landmark_to_station.items()},
    }

def _rank_station_match(query, station_name):
    """Computes a similarity score (0-100) between a user query and a station name."""
    q = normalize_text(query)
    s = normalize_text(station_name)
    if q == s:
        return 100
    if q in s:
        return 90 - (len(s) - len(q))
    if s in q:
        return 75 - (len(q) - len(s))
    return int(difflib.SequenceMatcher(None, q, s).ratio() * 70)

def _rank_landmark_match(query, landmark_name):
    """Similar to station matching, but tailored for landmarks."""
    q = normalize_text(query)
    l = normalize_text(landmark_name)
    if q == l:
        return 98
    if q in l or l in q:
        return 85
    return int(difflib.SequenceMatcher(None, q, l).ratio() * 68)

def resolve_place(user_input, graph, station_info):
    """
    Attempts to map a user-provided string (station name or landmark) to an exact
    station name. Performs exact match first, then normalized match, then fuzzy matching.
    Returns (station_name, explanation_message).
    """
    index = build_search_index(graph, station_info)
    raw = user_input.strip()
    norm = normalize_text(raw)

    # Exact station name match
    if raw in graph:
        return raw, f"Recognized as station: {raw}."
    # Normalized station name match
    if norm in index["station_norm_map"]:
        station = index["station_norm_map"][norm]
        return station, f"Recognized as station: {station}."
    # Normalized landmark match
    if norm in index["landmark_norm_map"]:
        station = index["landmark_norm_map"][norm]
        return station, f'Automatically matched landmark "{raw}" to nearby station: {station}.'

    # Fuzzy matching: collect station and landmark candidates with score >= 45
    station_candidates = []
    for station in index["stations"]:
        score = _rank_station_match(raw, station)
        if score >= 45:
            station_candidates.append((score, station))

    landmark_candidates = []
    for landmark, station in index["landmark_map"].items():
        score = _rank_landmark_match(raw, landmark)
        if score >= 45:
            landmark_candidates.append((score, landmark, station))

    # Sort candidates by score (descending), then by length (shorter preferred)
    station_candidates.sort(key=lambda x: (-x[0], len(x[1]), x[1]))
    landmark_candidates.sort(key=lambda x: (-x[0], len(x[1]), x[1], x[2]))

    best_station = station_candidates[0] if station_candidates else None
    best_landmark = landmark_candidates[0] if landmark_candidates else None

    # Choose the best match; station match gets a slight bias if scores are close
    if best_station and (not best_landmark or best_station[0] >= best_landmark[0] + 3):
        return best_station[1], f"No exact match found. Fuzzy-matched station name to: {best_station[1]}."
    if best_landmark:
        _, landmark, station = best_landmark
        return station, f'No exact match found. Fuzzy-matched landmark "{landmark}" to nearby station: {station}.'

    return None, f'Could not recognize "{raw}". Please enter a more complete station name or landmark.'

def ask_place(prompt, graph, station_info):
    """Repeatedly asks the user for a station or landmark name until valid."""
    while True:
        raw = input(prompt).strip()
        station, message = resolve_place(raw, graph, station_info)
        print(message)
        if station:
            return raw, station