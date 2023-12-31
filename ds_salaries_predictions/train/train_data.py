from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from preprocess.preprocess_data import *
import logging

logger = logging.getLogger(__name__) # Indicamos que tome el nombre del modulo
logger.setLevel(logging.DEBUG) # Configuramos el nivel de logging

formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s') # Creamos el formato

file_handler = logging.FileHandler('train_data.log') # Indicamos el nombre del archivo

file_handler.setFormatter(formatter) # Configuramos el formato

logger.addHandler(file_handler) # Agregamos el archivo


class SalaryDataPipeline:
    """
    A class representing the DS Salary  data processing and modeling pipeline.

    Attributes:
        NUMERICAL_VARS (list): A list of numerical variables in the dataset.
        CATEGORICAL_VARS_WITH_NA (list): A list of categorical variables with missing values.
        NUMERICAL_VARS_WITH_NA (list): A list of numerical variables with missing values.
        CATEGORICAL_VARS (list): A list of categorical variables in the dataset.
        SEED_MODEL (int): A seed value for reproducibility.

    Methods:
        create_pipeline(): Create and return the DS Salary data processing pipeline.
    """
    
    def __init__(self, seed_model, numerical_vars, categorical_vars_with_na,
                 numerical_vars_with_na, categorical_vars, selected_features):
        logger.info("Initializate the pipeline")
        self.SEED_MODEL = seed_model
        self.NUMERICAL_VARS = numerical_vars
        self.CATEGORICAL_VARS_WITH_NA = categorical_vars_with_na
        self.NUMERICAL_VARS_WITH_NA = numerical_vars_with_na
        self.CATEGORICAL_VARS = categorical_vars
        self.SEED_MODEL = seed_model
        self.SELECTED_FEATURES = selected_features
        
        
    def create_pipeline(self):
        """
        Create and return the Salary  data processing pipeline.

        Returns:
            Pipeline: A scikit-learn pipeline for data processing and modeling.
        """
        logger.debug("Begin the creation for pipeline")

        self.PIPELINE = Pipeline(
            [                   
                                ('dummy_vars', OneHotEncoder(variables=self.CATEGORICAL_VARS)), 
                                ('scaling', MinMaxScaler()),                   
                              ]
        )
        return self.PIPELINE
    
    def fit_linear_regression(self, X_train, y_train):
        logger.debug("Begin the linear regression training")
        """
        Fit a Linear Regression model using the predefined data preprocessing pipeline.

        Parameters:
        - X_train (pandas.DataFrame or numpy.ndarray): The training input data.
        - y_train (pandas.Series or numpy.ndarray): The target values for training.

        Returns:
        - linear_regression_model (LogisticRegression): The fitted Logistic Regression model.
        """
        linear_regression = LinearRegression()
        pipeline = self.create_pipeline()
        pipeline.fit(X_train, y_train)
        X_transform = pipeline.transform(X_train)
        linear_regression.fit(X_transform, y_train)
        return linear_regression
    
    
    def apply_pipeline_to_test_data(self, X_test):
        """
        Applies the data processing pipeline to the test data.

        Parameters:
            X_test (pd.DataFrame): Test input data.

        Returns:
            X_test_transformed (pd.DataFrame): Transformed test data using the pipeline.
        """
        logger.debug("Begin the transformation for the test data")
        pipeline = self.create_pipeline()
        pipeline.fit(X_test)
        X_test_transformed = pipeline.transform(X_test)
        return X_test_transformed