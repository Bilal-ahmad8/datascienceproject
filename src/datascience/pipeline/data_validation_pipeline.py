from src.datascience.components.data_validation import DataValidation
from src.datascience import logger
from src.datascience.config.configurations import ConfigurationManager


class DataValidationPipeline:
    def __init__(self):
        pass

    def start_data_validation(self):
        config = ConfigurationManager()
        datavalidationConfig = config.get_data_validation_config()
        data_validation = DataValidation(config=datavalidationConfig)
        data_validation.validate_data()