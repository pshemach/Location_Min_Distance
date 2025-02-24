import logging
from ortools.constraint_solver import pywrapcp
from tsp.data_model.load_data import load_distance_matrix
from tsp.constants import DEPOT

def tsp_manager(distance_matrix, locations):
    try:
        logging.info("Initializing TSP Manager with depot location.")
        depot_index = locations.index(DEPOT)
        
        manager = pywrapcp.RoutingIndexManager(
            len(distance_matrix), 1, depot_index
        )  # Single vehicle, depot at index 0
        
        logging.info("TSP Manager successfully created.")
        return manager
    except ValueError as ve:
        logging.error(f"Depot location not found in locations list: {str(ve)}")
        raise
    except Exception as e:
        logging.critical(f"Unexpected error in TSP Manager creation: {str(e)}")
        raise


# from ortools.constraint_solver import pywrapcp
# from tsp.data_model.load_data import load_distance_matrix
# from tsp.constants import DEPOT

# def tsp_manager(distance_matrix, locations):
#     depot_index = locations.index(DEPOT)

#     manager = pywrapcp.RoutingIndexManager(
#         len(distance_matrix), 1, depot_index
#     )  # Single vehicle, depot at index 0

#     return manager