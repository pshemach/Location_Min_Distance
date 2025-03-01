from fastapi import FastAPI, File, UploadFile, HTTPException
from tsp.data_model.load_data import load_distance_matrix
from tsp.solver.path_map import get_route_tsp
import io
from tsp.logger import logging

app = FastAPI()


@app.post("/solve_tsp")
async def solve_tsp(file: UploadFile = File(...)):
    try:
        if not file.filename.endswith(".csv"):
            logging.error("Invalid file format. Only CSV files are allowed.")
            raise HTTPException(status_code=400, detail="Invalid file format. Please upload a CSV file.")
        
        contents = await file.read()
        distance_matrix_path = io.StringIO(contents.decode("utf-8"))
        
        try:
            distance_matrix, locations = load_distance_matrix(distance_matrix_path)
            logging.info(f"Distance matrix loaded successfully. Locations: {locations}")
        except Exception as e:
            logging.error(f"Error loading distance matrix: {str(e)}")
            raise HTTPException(status_code=400, detail=f"Error loading distance matrix: {str(e)}")
        
        if not distance_matrix or not locations:
            logging.error("Invalid or empty distance matrix.")
            raise HTTPException(status_code=400, detail="Invalid or empty distance matrix.")
        
        try:
            route_order, total_distance = get_route_tsp(distance_matrix, locations)
        except Exception as e:
            logging.error(f"Error solving TSP: {str(e)}")
            raise HTTPException(status_code=500, detail=f"Error solving TSP: {str(e)}")
        
        logging.info(f"TSP solved successfully. Route: {route_order}, Total Distance: {total_distance}")
        return {
            "route_order": route_order,
            "total_distance": total_distance
        }
        
    except HTTPException as http_err:
        logging.error(f"HTTP error: {str(http_err)}")
        raise http_err
    except Exception as e:
        logging.critical(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

@app.get("/")
def home():
    logging.info("Home endpoint accessed.")
    return {"message": "TSP Solver API is running!"}
