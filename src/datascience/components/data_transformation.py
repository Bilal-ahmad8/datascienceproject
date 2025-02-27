import pandas as pd
from sklearn.model_selection import train_test_split
from src.datascience import logger
import os
from src.datascience.entity.config_entity import DataTransformationConfig



class DataTransformation:
    def __init__(self, config= DataTransformationConfig):
        self.config = config

    def transform_data(self):

        data = pd.read_csv("artifacts/data_ingestion/winequality-red.csv")
        train, test  = train_test_split(data, test_size=.2, random_state=42)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted data into Train and Test Sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)