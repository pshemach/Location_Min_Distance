import pandas as pd

def load_distance_matrix(distance_matrix_path):
    distance_matrix_df = pd.read_csv(distance_matrix_path, index_col=0)
    distance_matrix = distance_matrix_df.values
    locations = distance_matrix_df.index.tolist()
    return distance_matrix, locations

