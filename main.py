from metro_data import DATA_TEXT
from metro_input import load_data_from_text, ask_place
from metro_router import build_graph, find_routes
from metro_output import print_routes

def main():
    """
    Main entry point for the metro routing application.
    Orchestrates user input, core logic, and final output display.
    """
    # Initialize basic data structures
    metro_lines, transfer_times, station_info = load_data_from_text(DATA_TEXT)
    graph = build_graph(metro_lines)

    # Collect Origin and Destination
    start_raw, start = ask_place("Please enter the origin station or a nearby landmark: ", graph, station_info)
    target_raw, target = ask_place("Please enter the destination station or a nearby landmark: ", graph, station_info)

    if start == target:
        print("The origin and destination are the same!")
        return

    # Collect Routing Preference
    valid_prefs = {"time", "cost", "balanced", "transfer", "comfort", "walk", "accessible"}
    while True:
        preference = input("Please enter your preference (time/cost/balanced/transfer/comfort/walk/accessible): ").strip().lower()
        if preference in valid_prefs:
            break
        print("Invalid preference mode. Please enter it again.")

    # Collect Departure Time
    while True:
        dep_str = input("Please enter the departure time (HH:MM): ").strip()
        try:
            h, m = map(int, dep_str.split(":"))
            if 0 <= h <= 23 and 0 <= m <= 59:
                departure_time = dep_str
                break
        except Exception:
            pass
        print("Invalid time format. Please use HH:MM.")

    # Collect Optional Parameters
    preferred_entry = input("Please enter the preferred entrance (optional, e.g. Gate A): ").strip()
    desired_landmark = input("Please enter the destination landmark (optional): ").strip()

    # Collect Budget
    while True:
        budget_input = input("Please enter the maximum budget in HK$ (optional): ").strip()
        if not budget_input:
            max_budget = None
            break
        try:
            # Cast budget to float to match the new fare format
            max_budget = float(budget_input)
            if max_budget >= 0:
                break
            print("The budget cap must be a non-negative number. Please enter it again.")
        except Exception:
            print("The budget cap must be a non-negative number. Please enter it again.")

    # Collect Simulation Mode
    while True:
        mode = input("Please choose the departure mode (accurate/estimate, default: accurate): ").strip().lower()
        if mode == "":
            schedule_mode = "accurate"
            break
        if mode in ("accurate", "estimate"):
            schedule_mode = mode
            break
        print("Invalid departure mode. Please enter accurate or estimate.")

    # Collect Accessibility Needs
    acc_input = input("Prioritize fewer stairs / accessibility? (y/n, default: n): ").strip().lower()
    accessibility = (acc_input == "y")

    # Run Routing Algorithm
    routes = find_routes(
        graph=graph,
        lines=metro_lines,
        transfer_times=transfer_times,
        station_info=station_info,
        start=start,
        target=target,
        departure_time=departure_time,
        k=3,
        preference=preference,
        max_budget=max_budget,
        preferred_entry=preferred_entry,
        desired_landmark=desired_landmark,
        schedule_mode=schedule_mode,
        accessibility=accessibility,
    )

    # Print Results
    print_routes(routes, f"Top 3 recommended routes from {start} to {target}", preference, max_budget, schedule_mode)

if __name__ == "__main__":
    main()