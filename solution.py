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

def route(van_stats, packages):
    packages = sorted(packages, key=lambda x: abs(x[0])) # Sorting packages by distance from starting point
    

def find_optimal_route_for_single_van(van_stats: list[tuple[int, int]], packages: list[tuple[int, int, int]]) -> tuple[
    tuple[int, int], list[tuple[int, str]], int, int]:
    # TODO: Replace this with a real implementation:
    return (
        (9, 8),
        [(0, 'start'), (-1, 'pick'), (-2, 'pick'), (5, 'drop'), (9, 'drop'), (6, 'pick'), (2, 'drop'), (0, 'end')],
        22,
        176
    )

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