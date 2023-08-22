# ITESM-MLOps-Project
This repository contains the files related to first part of the final proyect 

Student ID : A01688409

Student Name : Luis Fernandez Pérez

Teacher: Dr. Carlos Noé López Mejía

This project uses the following dataset : 

https://www.kaggle.com/datasets/arnabchaki/data-science-salaries-2023/

## About the project

The overall goal of this project is to build a robust and reproducible MLOps workflow for developing, training, and deploying machine learning models. A linear regression model will be used as a proof of concept due to its simplicity, and it will be applied to the Titanic data set to predict the probability of survival of a passenger based on certain characteristics.

This project covers the following topics:

1. **Key concepts of ML systems**  
The objective of this module is to give an introduction to MLOps, life cycle and architecture examples is also given.

2. **Basic concepts and tools for software development**  
This module focuses on introducing the principles of software development that will be used in MLOps. Consider the configuration of the environment, tools to use, and best practices, among other things.

3. **Development of ML models**  
This module consists of showing the development of an ML model from experimentation in notebooks, and subsequent code refactoring, to the generation of an API to serve the model.

4. **Deployment of ML models**  
The objective of this module is to show how a model is served as a web service to make predictions.

5. **Integration of concepts**  
This module integrates all the knowledge learned in the previous modules. A demo of Continuous Delivery is implemented.


# Data-Science-Job-Salaries Predective Model - Project Overview

The "Data Science Salaries" dataset provides valuable insights into the compensation trends and variations in the field of data science from 2020 to 2023. This dataset encompasses a comprehensive collection of salary information from various industries, organizations, and geographic regions, enabling data professionals, researchers, and organizations to analyze and understand the prevailing salary landscape in the data science domain during this four-year period. By examining this dataset, one can gain a deeper understanding of the factors influencing data science salaries, such as job roles, experience levels, educational backgrounds, and geographical locations. The dataset serves as a valuable resource for individuals seeking career guidance, companies aiming to benchmark their compensation strategies, and researchers investigating the evolving dynamics of the data science job market.

**Features list**

1. `work_year`: The year the salary was paid.
2. `experience_level`: The experience level in the job during the year.
    - `EN` > Entry-level / Junior
    - `MI` > Mid-level / Intermediate
    - `SE` > Senior-level / Expert
    - `EX` > Executive-level / Director
3. `employment_type`: The type of employment for the role.
    - `PT` > Part-time
    - `FT` > Full-time
    - `CT` > Contract
    - `FL` > Freelance
4. `job_title`: The role worked in during the year.
5. `salary`: The total gross salary amount paid.
6. `salary_currency`: The currency of the salary paid as an ISO 4217 currency code.
7. `salaryinusd`: The salary in USD.
8. `employee_residence`: Employee's primary country of residence during the work year as an ISO 3166 country code.
9. `remote_ratio`: The overall amount of work done remotely.
10. `company_location`: The country of the employer's main office or contracting branch.
11. `company_size`: The median number of people that worked for the company during the year.


## Scope
This project represents a proof of concept aiming to develop a basic framework for a school project focused on salary prediction using dataset analysis. The scope intentionally includes minimal essential components to demonstrate the feasibility of predicting salaries based on the dataset. However, it should be noted that this proof of concept does not encompass an exhaustive development process and does not represent the most optimal approach to salary prediction. The primary objective is to provide a foundational understanding of the predictive modeling concept within the context of the dataset, serving as a starting point for further exploration and refinement.


### Links to experiments like notebooks

You can find the Titanic experiments here:

* [1-Data_Science_Salaries_Advanced_EDA.ipynb](docs/notebooks/1-Data_Science_Salaries_Advanced_EDA.ipynb)
* [2-DS_Salary_Full_EDA_Geo_Cluster_XGboost.ipynb](docs/notebooks/2-DS_Salary_Full_EDA_Geo_Cluster_XGboost.ipynb)
* [3-EDA_on_Data_Science_Salaries.ipynb](docs/notebooks/3-EDA_on_Data_Science_Salaries.ipynb)



# About the project requirements and venv
This project was developed using Python 3.10.9 .

Check the **requirements.txt** file for information on the packages' versions used in the project.

Check the **requirements_extended.txt** file for information on all the packages' versions used in the development.

To create virtual environment and install requirements use the following lines

 ```bash
python3.10 -m venv refactor_salarios
 ```

```bash
.\refactor_salarios\Scripts\activate
```

```bash
pip install -r requirements.txt
```

## Model training from a main file

To train the Logistic Model, only run the following code:

```bash
python.exe ds_salaries_predictions/ds_salaries_predictions.py
```

Output:

```bash
MAPE: 28.25932873960135
Model saved in ./models/linear_regression_output.pkl
```

## Execution of unit tests (Pytest)


### Test location

You can find the test location in the [test](tests) folder, and the following tests:

* Test `test_missing_indicator_transform`:  
Test the `transform` method of the MissingIndicator transformer.

* Test `test_missing_indicator_fit`:  
Test the `fit` method of the MissingIndicator transformer.

* Test `test_csv_file_existence`:  
Test case to check if the CSV file exists.

* Test `test_model_existence`:  
Test to validate the existence of a `.pkl` model file.

# DESCRIBE the directory Structure in the project

# Main file

The main file named *main.py* has all the functions needed to solve the objective. 

This file uses funcions from the modules in the project folders.

## Load Module

This module keeps the processes to import the dataset. 

We use a Dataset Copy of the original in a repo in git, because kaggle don´t have the raw data

The current functionality of this project is :
 
1. Download the dataset from the url from the 'https://raw.githubusercontent.com/luisfp2000/proyecto_final/main/Dataset/ds_salaries.csv'

1. Copy you local path to the dataset in the variable **FILE_PATH** in the *main.py* file

1. After using the load functionality in the *main.py* file , delete the dataset from the data folder in order to avoid commiting with file in the project. This project can't handle large files.

## Preprocess

This module keeps the transformations done to the dataset.

## Train 

This module holds the Pipeline to preprocess the dataset and the models methods that are going to be trained with the data.

## Models 

The main file export the trained model in this file to keep the results.

## Test

This module holds test to validate the functionalities in the other modules.

It has its own ReadMe

## Notebook

This folder keeps the original notebook


## api

This folder contain the api example with uvicorn server


## Usage

### Individual Fastapi and Use Deployment

* Run the next command to start the ds_salaries API locally

    ```bash
    uvicorn ds_salaries_predictions.api.main:app --reload
    ```

### Checking endpoints
1. Access `http://127.0.0.1:8000/`, you will see a message like this `DS Salaries Predictor is all ready to go!`

2. Access `http://127.0.0.1:8000/docs`

3. Try running the predict endpoint by writing the values: 
```bash
{
  "experience_level": "Expert",
  "employment_type": "Full-Time",
  "job_title": "Principal Data Scientist",
  "employee_residence": "ES",
  "company_location": "ES",
  "company_size": "S",
  "remote_ratio": 50
}
```

The endpoint return the valor of prediction and the values used for that, you will see a message like this `"Resultado predicción: [136987.83103204] for data: ['Expert', 'Full_Time', 'Principal Data Scientist', 'ES', 'ES', 'S', 50.0]"`

4. Try running the predict endpoint, you will see a message like this `"Trained model ready to go!"`



### Individual deployment of the API with Docker and usage

#### Build the image

* Ensure you are in the `ds_salaries_predictions` directory (root folder).
* Run the following code to build the image:

    ```bash
    docker build -t ds-salaries-image app/
    ```

* Inspect the image created by running this command:

    ```bash
    docker images
    ```

    Output:

    ```bash
    REPOSITORY          TAG       IMAGE ID       CREATED          SIZE
    ds-salaries-image   latest    a6c51bedf9c0   18 seconds ago   495MB
    ```

#### Run ds salaries REST API

1. Run the next command to start the `ds-salaries-image` image in a container.

    ```bash
    docker run -d --rm --name ds_salaries-c -p 8000:8000 ds-salaries-image
    ```
    
    Output:

    ```bash
    ds-salaries-image
    0f2e31e47f70768c50043b53e2d5e44d3c713fcc0047dab77c32861e4c9a67fd
    ```

2. Check the container running.

    ```bash
    docker ps -a
    ```

    Output:

    ```bash
    CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS          PORTS                    NAMES
    53d78fb5223f  ds-salaries-image     "uvicorn main:app --…"   19 seconds ago   Up 18 seconds   0.0.0.0:8000->8000/tcp   ds_salaries-c
    ```

#### Checking endpoints

1. Access `http://127.0.0.1:8000/`, and you will see a message like this `"Titanic classifier is all ready to go!"`
2. A file called `main_api.log` will be created automatically inside the container. We will inspect it below.
3. Access `http://127.0.0.1:8000/docs`, the browser will display something like this:
    ![FastAPI Docs](docs/imgs/fast-api-docs.png)

4. Try running the following predictions with the endpoint by writing the following values:
    * **Prediction 1**  
        Request body

        ```bash
        {
        "experience_level": "Expert",
        "employment_type": "Full-Time",
        "job_title": "Principal Data Scientist",
        "employee_residence": "ES",
        "company_location": "ES",
        "company_size": "S",
        "remote_ratio": 50
        }
        ```

        Response body
        The output will be:

        ```bash
         `"Resultado predicción: [136987.83103204] for data: ['Expert', 'Full_Time', 'Principal Data Scientist', 'ES', 'ES', 'S', 50.0]"`
        ```

    * **Prediction 2**  
        Request body

        ```bash
        {
        "experience_level": "Junior",
        "employment_type": "Partial",
        "job_title": "Principal Data Scientist",
        "employee_residence": "MX",
        "company_location": "MX",
        "company_size": "L",
        "remote_ratio": 30
        }
        ```

        Response body
        The output will be:

        ```bash
        `"Resultado predicción: [139212.73483592] for data: ['Junior', 'Partial', 'Principal Data Scientist', 'MX', 'MX', 'L', 30.0]"`
        ```


