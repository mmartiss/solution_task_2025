#greedy algo

def choose_next_package(van, van_position, packages, picked_up, dropped_off,
    current_load, route, route_length, fuel_consumed):
    """
    choose_next_package function chooses the next package to be picked up 
    or dropped off. It chooses the closest package to the van's current
    position and checks if it fits in the van. If not, it checks if it
    can drop off a package. If a package is picked up, it is added to the
    route and the van's current position is updated. 

    Args:
        van, van_position, packages, picked_up, dropped_off,
        current_load, route, route_length, fuel_consumed
    Returns:
        nearest_location, route, route_length, fuel_consumed, current_load, van_position
    """
    nearest_location = None
    min_distance = float('inf')  
    # Make it infinite, so we would have something to compare to
    action = None # Pick or drop, also tmp
    package_index = None

    # Iterations through all packages and extraction of data from packages
    for i, (pickup, drop, weight) in enumerate(packages):
        # Choose the closest one and if it fits
        if i not in picked_up and current_load + weight <= van[0]: 
            distance = abs(van_position - pickup)
            if(distance < min_distance):
                min_distance = distance
                nearest_location = pickup
                action = "pick" # Setting the acrtion
                package_index = i 
        # If its taken but not dropped off
        elif i in picked_up and i not in dropped_off:
            distance = abs(van_position - drop)
            if(distance < min_distance):
                min_distance = distance
                nearest_location = drop
                action = "drop"
                package_index = i
    
    if nearest_location is not None:
        # Adding to route
        route.append((nearest_location, action))
        route_length += min_distance
        van_position = nearest_location
        # fuel_consumed += fuel_consumption(van[1], min_distance, current_load, van[0])
        fuel_consumed += van[1] * min_distance
        picked_up.append(package_index) if action == "pick" else dropped_off.append(package_index)
        current_load += packages[package_index][2] if action == "pick" else -packages[package_index][2]

    return nearest_location, route, route_length, fuel_consumed, current_load, van_position

def find_optimal_route_for_single_van(van_stats: list[tuple[int, int]], packages: 
    list[tuple[int, int, int]]) -> tuple[tuple[int, int], list[tuple[int, str]], int, int]:
    """
    find_optima_route_for_single_van function chooses the most fuel efficient route and van
    
    It takes output from choose_next_package function and iterates through all vans to find the
    most fuel efficient route. 
    It then returns the chosen van, route, route length and fuel consumed.

    Args:
        van_stats, packages

    Returns:
        chosen_van, chosen_route, route_length, minimum_fuel

    Asked format for the output:
        (9, 8),
        [(0, 'start'), (-1, 'pick'), (-2, 'pick'), (5, 'drop'), (9, 'drop'), (6, 'pick'), (2, 'drop'), (0, 'end')],
        22,
        176
    """
    # TODO: Replace this with a real implementation:
    chosen_van = None
    chosen_route = None

    minimum_fuel = float('inf')

    for van in van_stats:
        picked_up = []
        dropped_off = []
        route = [(0, "start")]
        route_length = 0
        fuel_consumed = 0
        van_position = 0
        current_load = 0
        nearest_location = None

        while len(dropped_off) < len(packages):
            # choose_next_package function's output
            nearest_location, route, route_length, fuel_consumed, current_load, 
            van_position = choose_next_package(
                van, van_position, packages, picked_up, dropped_off, current_load, route, 
                route_length, fuel_consumed
            )
            if nearest_location is None:
                break
        
        route.append((0, "end"))
        route_length += abs(van_position - 0)
        fuel_consumed += van[1] * abs(van_position - 0)

        if(fuel_consumed < minimum_fuel):
            minimum_fuel = fuel_consumed
            chosen_van = van
            chosen_route = route

    return chosen_van, chosen_route, route_length, minimum_fuel

    # return (
    #     (9, 8),
    #     [(0, 'start'), (-1, 'pick'), (-2, 'pick'), (5, 'drop'), (9, 'drop'), (6, 'pick'), (2, 'drop'), (0, 'end')],
    #     22,
    #     176
    # )

if __name__ == "__main__":
    # This is an example test for Base goal. When evaluating the task, more will be added:
    selected_van, optimal_route, route_length, fuel_consumption = find_optimal_route_for_single_van(
        [(10, 10), (9, 8)],  [(-1, 5, 4), (6, 2, 9), (-2, 9, 3)]
    )

    print(selected_van)
    print(optimal_route)
    print(route_length)
    print(fuel_consumption)

    # assert selected_van == (9, 8)
    # assert optimal_route == [
    #     (0, 'start'), (-1, 'pick'), (-2, 'pick'), (5, 'drop'), (9, 'drop'), (6, 'pick'), (2, 'drop'), (0, 'end')
    # ]
    # assert route_length == 22
    # assert fuel_consumption == 176

    # print("ALL TESTS PASSED")
    