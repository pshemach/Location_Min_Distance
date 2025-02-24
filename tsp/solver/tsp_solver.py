from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from tsp.solver.manager import tsp_manager

def get_solution(distance_matrix_path):
    manager, distance_matrix, locations = tsp_manager(distance_matrix_path)
    
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return int(distance_matrix[from_node][to_node])
    
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    )

    solution = routing.SolveWithParameters(search_parameters)

    return solution, routing, manager, distance_matrix, locations