#greedy algo

def choose_next_package(van, van_position, packages, picked_up, dropped_off, current_load, route, route_length, fuel_consumed):
    nearest_location = None
    min_distance = float('inf')  #nustatom infinite, kad butu su kuom palyginti
    action = None # pick or drop, also tmp
    package_index = None

    # iteruojam per visas packages ir tuo paciu istraukiam data is packages
    for i, (pickup, drop, weight) in enumerate(packages):
        #rinktis arciausia ir jei telpa
        if i not in picked_up and current_load + weight <= van[0]: 
            distance = abs(van_position - pickup)
            if(distance < min_distance):
                min_distance = distance
                nearest_location = pickup
                action = "pick" #nustatom koks action
                package_index = i #issisaugom, kad veliau zinotume kuris paimtas
        # jei paimtas, bet nepristatytas
        elif i in picked_up and i not in dropped_off:
            distance = abs(van_position - drop)
            if(distance < min_distance):
                min_distance = distance
                nearest_location = drop
                action = "drop"
                package_index = i
    
    if nearest_location is not None:
        # pridedam i route
        route.append((nearest_location, action))
        route_length += min_distance
        van_position = nearest_location
        # fuel_consumed += fuel_consumption(van[1], min_distance, current_load, van[0])
        fuel_consumed += van[1] * min_distance
        picked_up.append(package_index) if action == "pick" else dropped_off.append(package_index)
        current_load += packages[package_index][2] if action == "pick" else -packages[package_index][2]

    return nearest_location, route, route_length, fuel_consumed, current_load, van_position

def find_optimal_route_for_single_van(van_stats: list[tuple[int, int]], packages: list[tuple[int, int, int]]) -> tuple[
    tuple[int, int], list[tuple[int, str]], int, int]:
    # TODO: Replace this with a real implementation:
    chosen_van = None
    chosen_route = None

    minimum_fuel = float('inf')

    for van in van_stats:
        # man sios funkcijos riekia, nes skiriasi vans capacity ir fuel consumption
        picked_up = []
        dropped_off = []
        route = [(0, "start")]
        route_length = 0
        fuel_consumed = 0
        van_position = 0
        current_load = 0
        nearest_location = None

        # cia kviesiu choose_next_package function
        #reikia palyginti vieno van su kitu keliones, by fuel ir distance
        # kadangi tai not nercursive fukcija, su while loop eisim per ja, maziau resursu naudots

        while len(dropped_off) < len(packages):
            # choose_next_package funkcijos output
            nearest_location, route, route_length, fuel_consumed, current_load, van_position = choose_next_package(
                van, van_position, packages, picked_up, dropped_off, current_load, route, route_length, fuel_consumed
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








