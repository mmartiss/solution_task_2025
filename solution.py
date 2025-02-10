def fuel_consumption(base_fuel, distance, total_weight, max_capacity):
    """
    fuel_consumption does the calculation of total fuel needed for a trip based on base fuel, 
    distance, total weight and max capacity

    base_fuel: int, initial fuel consumption per unit distance without any load
    distance: int, distance to be travelled
    total_weight: int, total weight of the packages
    max_capacity: int, maximum capacity of the van

    return: int, total fuel needed for the trip
    """
    return base_fuel * distance * (1 + total_weight / max_capacity)

# tikslo funckija, kaip mawtematine vektorine funkcija
#  arba kriterinis, apsirasai dvi funkcijas, kuri apibrezia pickup ir drop

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
    
    # jei radom artimiausia vieta automatiskai atrinke ar paimtas ar ne, ir ka daryti
    #!!!!!
    # reikia logiskai isnagrineti ar tai tikriausiai geriausias action ir kelio pasirinkimas

    if nearest_location is not None:
        # pridedam i route
        route.append((nearest_location, action))
        route_length += min_distance
        
        fuel_consumed += fuel_consumption(van[1], min_distance, current_load, van[0])
        picked_up.append(package_index) if action == "pick" else dropped_off.append(package_index)
        current_load += packages[package_index][2] if action == "pick" else -packages[package_index][2]

    return nearest_location, route, route_length, fuel_consumed, current_load
    # for i in pick_up_locations:
    # # patikrinti ar package nebuvo paimtas ir ar telpa i van
    #     if i not in picked_up and current_load + package_weight[i] <= van[0]: 
    #         distance = abs(van_position - i)
    #         if(distance < min_distance):
    #             min_distance = distance
    #             nearest_location = i

    # route.append((nearest_location, 'pick'))
    # route_length += min_distance
    # fuel_consumed += fuel_consumption(van[1], min_distance, package_weight[pick_up_locations.index(nearest_location)], van[0])



#heuristinis recursive backracking algo
def find_optimal_route_for_single_van(van_stats: list[tuple[int, int]], packages: list[tuple[int, int, int]]) -> tuple[
    tuple[int, int], list[tuple[int, str]], int, int]:
    # TODO: Replace this with a real implementation:
    chosen_van = None

    for van in van_stats:
        # man sios funkcijos riekia, nes skiriasi vans capacity ir fuel consumption
        picked_up = []
        dropped_off = []
        route = [(0, "start")]
        route_length = 0
        fuel_consumed = 0
        van_position = 0
        current_load = 0

        # cia kviesiu choose_next_package function
        #reikia palyginti vieno van su kitu keliones, by fuel ir distance





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

    assert selected_van == (9, 8)
    assert optimal_route == [
        (0, 'start'), (-1, 'pick'), (-2, 'pick'), (5, 'drop'), (9, 'drop'), (6, 'pick'), (2, 'drop'), (0, 'end')
    ]
    assert route_length == 22
    assert fuel_consumption == 176

    print("ALL TESTS PASSED")