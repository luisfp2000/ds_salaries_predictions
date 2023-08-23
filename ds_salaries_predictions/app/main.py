import logging
import os
import sys

import logging
import pandas as pd
from fastapi import FastAPI
from starlette.responses import JSONResponse

from predictor.predict import ModelPredictor
from models.models import DSSalariesPrediction

import subprocess
# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)


logger = logging.getLogger(__name__) # Indicamos que tome el nombre del modulo
logger.setLevel(logging.DEBUG) # Configuramos el nivel de logging

formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s') # Creamos el formato

file_handler = logging.FileHandler('main_api.log') # Indicamos el nombre del archivo

file_handler.setFormatter(formatter) # Configuramos el formato

logger.addHandler(file_handler) # Agregamos el archivo


PATH_COLS="models/train_data.csv"

app = FastAPI()

@app.get('/', status_code=200)
async def healthcheck():
    logger.info('DS Salaries Predictor is all ready to go!')
    return 'DS Salaries Predictor is all ready to go!'


@app.post('/predict')

def predict(ds_salaries_features: DSSalariesPrediction) -> JSONResponse: 
    
    predictor = ModelPredictor("ml_models/linear_regression_output.pkl")
    
    X = [ds_salaries_features.experience_level,
         ds_salaries_features.employment_type,
         ds_salaries_features.job_title,
         ds_salaries_features.employee_residence,
         ds_salaries_features.company_location,
         ds_salaries_features.company_size,
         ds_salaries_features.remote_ratio]
    
    # Valores categóricos y numéricos del registro
    categorical_values = {
        'experience_level_'+ds_salaries_features.experience_level:      ds_salaries_features.experience_level,
        'employment_type_'+ds_salaries_features.employment_type:        ds_salaries_features.employment_type,
        'job_title_'+ds_salaries_features.job_title:                    ds_salaries_features.job_title,
        'employee_residence_'+ds_salaries_features.employee_residence:  ds_salaries_features.employee_residence,
        'company_location_'+ds_salaries_features.company_location:      ds_salaries_features.company_location,
        'company_size_'+ds_salaries_features.company_size:              ds_salaries_features.company_size,
        }

    remote_ratio = ds_salaries_features.remote_ratio/100

    pd_struct_to_model = pd.read_csv(PATH_COLS)

    # one-hot encoding columns
    column_names = pd_struct_to_model.columns.tolist()

    # call to function for obtain the dataframe with flags
    encoded_df = encode_categorical_values(remote_ratio, column_names, categorical_values)
    
    row_series = encoded_df.iloc[0]
    row_list = row_series.tolist()

    prediction = predictor.predict([row_list])
    
    logger.info(f"Input values: {[X]}")
    logger.info(f"Resultado predicción: {prediction}")

    return JSONResponse(f"Resultado predicción: {prediction} for data: {X}")


@app.get("/train_model", status_code=200)
def train_model():
    
    logger.info(f"The model is training")
    # Execute the  archivo ds_salaries_predictions.py how a process
    subprocess.run(["python", "ds_salaries_predictions/ds_salaries_predictions.py"])

    
    logger.info(f"The model was train success")   
 
    return "Trained model ready to go!"



    """
    Encodes categorical values into a one-hot encoded DataFrame row.

    Args:
        remote_ratio_value (float): The remote ratio value for the row.
        column_names (list): List of column names for the one-hot encoded DataFrame.
        categorical_values (dict): Dictionary containing categorical column names as keys and corresponding values.

    Returns:
        pandas.DataFrame: A DataFrame with the encoded row.
    """

def encode_categorical_values(remote_ratio_value, column_names, categorical_values):
    # Create a DF empty with the one-hot encoding
    encoded_df = pd.DataFrame(columns=column_names)
    
    row = [0] * len(column_names)

    row[0] = remote_ratio_value

    for col_name, value in categorical_values.items():
        if col_name in column_names:
            index = column_names.index(col_name)
            row[index] = 1
    
    encoded_df.loc[0] = row
    
    return encoded_df

