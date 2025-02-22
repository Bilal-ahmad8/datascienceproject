from urllib import request
from src.datascience import logger
import zipfile
from src.datascience.entity.config_entity import (DataIngestionConfig)
import os

#components - Data Ingestion

class DataIngestion:
    def __init__(self, config=DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f'{filename} download! with the following info {header}')

        else:
            logger.info('File already exists')


    def extract_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zrf:
            zrf.extractall(unzip_path)