"""
# Task:
Implement a route planning algorithm.

# Description:
Write a Python program that calculates the optimal route plan given a fleet of vans to deliver packages.
The program should determine the most fuel efficient route based on distances while considering the capacity of each
van, van fuel consumption and the weight of the packages.

# Constraints:
1. Each van has a specified capacity.
2. Each package has a pickup location, delivery location, and weight.
3. Locations are one dimensional (straight line).
4. Vans can pick up and deliver multiple packages, ensuring their capacity is not exceeded.
5. Vans can drop a package only at destination.
6. All packages must be delivered by the end of the day.
7. All vans start and end the day at central warehouse (0).
8. Max 5 packages might need to be delivered during the day.
9. Max 3 vans might be given as a fleet.
10. In case of multiple best routes, provide any one of them.
11. Do not use any 3rd party libraries. You can use Python standard libraries.

# Goals:
1. [Base] Calculate the most fuel efficient route if only a single van from the fleet would operate during the
   day (others remain parked). You need to determine which van is the most suitable for the day.
2. [Optional - Karma points] Calculate the most fuel efficient routes combination if all vans would be operational
   during the day. You'll need to create a function `find_optimal_route_for_multiple_vans`.

# Input Format:
- van_stats: A list where each element specifies the capacity of a van and fuel units consumed for 1 distance unit
    - van_stats = [(10, 10), (9,8)]
- packages: A list of tuples, where each tuple represents a package with (pickup location, delivery location, weight).
    - packages = [(-1, 5, 4), (6, 2, 9), (-2, 9, 3)]

# Sample Input:
van_stats = [(10, 10), (9,8)]
packages = [(-1, 5, 4), (6, 2, 9), (-2, 9, 3)]

# Sample Output for Base Goal:
- Selected Van: (9, 8)
- Optimal Route: [
      (0, "start"), (-1, "pick"), (-2, "pick"), (5, "drop"), (9, "drop"), (6, "pick"), (2, "drop"), (0, "end")
  ]
- Route Length: 22
- Fuel Consumption: 176
"""

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
