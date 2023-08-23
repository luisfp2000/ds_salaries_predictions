import os
import logging
import pytest


logger = logging.getLogger(__name__) # Indicamos que tome el nombre del modulo
logger.setLevel(logging.DEBUG) # Configuramos el nivel de logging

formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s') # Creamos el formato

file_handler = logging.FileHandler('test_file.log') # Indicamos el nombre del archivo

file_handler.setFormatter(formatter) # Configuramos el formato

logger.addHandler(file_handler) # Agregamos el archivo





def does_csv_file_exist(file_path):
    """
    Check if a CSV file exists at the specified path.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)

def test_csv_file_existence():

    """
    Test case to check if the CSV file exists.
    """
  
    # Provide the path to your CSV file that needs to be tested
    # refactored folder
    REFACTORED_DIRECTORY = "ds_salaries_predictions/"

    os.chdir(REFACTORED_DIRECTORY)
    csv_file_path = "data/ds_salaries.csv"

    # Call the function to check if the CSV file exists
    file_exists = does_csv_file_exist(csv_file_path)
    # Use Pytest's assert statement to check if the file exists
    assert file_exists == True, f"The CSV file at '{csv_file_path}' does not exist."



def test_model_existence():
    """
    Test to validate the existence of a .pkl model file.

    This test function checks whether the specified .pkl model file exists
    in the specified directory.

    Raises:
        AssertionError: If the model file doesn't exist.

    Usage:
        Run this test using the pytest command:
        pytest test_model_existence.py
    """
    model_filename = "linear_regression_output.pkl"
    MODEL_DIRECTORY = "models"
    model_path = os.path.join(MODEL_DIRECTORY, model_filename)
    print(model_path)
    assert os.path.exists(model_path), f"Model file '{model_filename}' does not exist."

if __name__ == "__main__":
    # Run the test function using Pytest
    pytest.main([__file__])

