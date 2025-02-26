import os
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib
import mlflow.sklearn
import numpy as np
from src.datascience.entity.config_entity import ModelEvaluationConfig
from src.datascience.utils.common import save_json
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
os.environ["MLFLOW_TRACKING_URI"]= os.getenv('MLFLOW_URI')
os.environ["MLFLOW_TRACKING_USERNAME"]=os.getenv('NAME')
os.environ["MLFLOW_TRACKING_PASSWORD"]= os.getenv('SECRET_ACCESS_KEY')


class ModelEvaluation:
    def __init__(self, config= ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2Score = r2_score(actual,pred)
        return rmse, mae, r2Score
    

    def log_into_mlflow(self):
        data = pd.read_csv(self.config.test_data_path)

        test_x = data.drop([self.config.target_column], axis=1)
        test_y = data[[self.config.target_column]]

        model = joblib.load(self.config.model_path)

        mlflow.set_registry_uri(self.config.mlflow_uri)
        #tracking_uri_type = urlparse(mlflow.get_tracking_uri()).scheme
        
        with mlflow.start_run():
            pred = model.predict(test_x)
            
            (rmse, mae, r2) = self.eval_metrics(test_y, pred)

            scores = {'rmse': rmse, "mae": mae, 'r2_score': r2}

            save_json(path=Path(self.config.model_metrics_name), data=scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(scores)

            mlflow.sklearn.log_model(model,"model")