def print_routes(routes, title="Recommended Routes", preference="time", max_budget=None, schedule_mode="accurate"):
    """
    Formats and outputs the calculated navigation routes to the console.
    Information regarding 'fare units' has been removed; only the total estimated fare is displayed.
    """
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)
    print(f"Preference: {preference}")
    print(f"Schedule mode: {schedule_mode}")
    if max_budget is not None:
        print(f"Budget cap: HK${max_budget}")
    print("-" * 72)

    if not routes:
        print("No routes found that satisfy the current constraints.")
        return

    for idx, route in enumerate(routes, 1):
        print(f"\nRoute {idx}")
        print("-" * 72)
        print(f"Arrival time: {route.arrival_time}")
        print(f"Total travel time: {round(route.walk_time + route.in_vehicle_time, 1)} min")
        # Display the calculated real-world fare
        print(f"Total fare: HK${route.total_cost:.1f}")
        print(f"Transfers: {route.transfer_count}")
        print(f"Walking time: {round(route.walk_time, 1)} min")
        print(f"Pure in-vehicle time: {round(route.in_vehicle_time, 1)} min")
        print(f"Average crowding: {route.avg_crowding}")
        print(f"High-crowding minutes: {route.high_crowding_minutes} min")
        print(f"Stair burden (transfers): {route.stair_burden}")
        print(f"Estimated carbon saved: {route.carbon_saved_kg} kg")
        print(f"Entry recommendation: {route.entry_msg}")
        print(f"Exit recommendation: {route.exit_reason}")
        print("Path: " + " -> ".join(route.stations))
        print("Instructions:")
        for step_no, instruction in enumerate(route.instructions, 1):
            print(f"  {step_no}. {instruction}")