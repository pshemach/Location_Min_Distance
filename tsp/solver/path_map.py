from tsp.solver.tsp_solver import get_solution

def get_route_tsp(distance_matrix_path):
    solution, routing, manager, distance_matrix, locations = get_solution(distance_matrix_path)
    if solution is None:
        index = routing.Start(0)
        total_distance = 0
        route_order = []

        while not routing.IsEnd(index):
            route_order.append(locations[manager.IndexToNode(index)])
            next_index = solution.Value(routing.NextVar(index))
            total_distance += distance_matrix[manager.IndexToNode(index)][
                manager.IndexToNode(next_index)
            ]
            index = next_index

        route_order.append(locations[manager.IndexToNode(index)])  # Return to depot

        print(" -> ".join(route_order))
        print(f"Total Distance: {total_distance:.2f} km")

        return route_order, total_distance
    else:
        print("No solution found.")



