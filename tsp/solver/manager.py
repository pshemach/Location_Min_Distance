from ortools.constraint_solver import pywrapcp
from tsp.data_model.load_data import load_distance_matrix
from tsp.constants import DEPOT

def tsp_manager(distance_matrix_path):
    distance_matrix, locations = load_distance_matrix(distance_matrix_path)
    depot_index = locations.index(DEPOT)

    manager = pywrapcp.RoutingIndexManager(
        len(distance_matrix), 1, depot_index
    )  # Single vehicle, depot at index 0

    return manager, distance_matrix, locations