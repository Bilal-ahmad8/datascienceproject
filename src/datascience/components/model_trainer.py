import os
import pandas as pd
from sklearn.linear_model import ElasticNet
from src.datascience import logger
import joblib
from src.datascience.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        train_x = pd.read_csv(self.config.train_data_path)
        train_y = train_x.pop(self.config.target_column)

        test_x = pd.read_csv(self.config.test_data_path)
        test_y = test_x.pop(self.config.target_column)

        En = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42) 
        En.fit(train_x, train_y)
        logger.info("Model Trained!")

        joblib.dump(En, os.path.join(self.config.root_dir, self.config.model_name))
        logger.info('Model Dumped!')