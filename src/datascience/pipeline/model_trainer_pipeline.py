from src.datascience.components.model_trainer import ModelTrainer
from src.datascience.config.configurations import ConfigurationManager
from src.datascience import logger

STAGE_NAME = 'Model Trainer Stage'

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def start_model_training(self):
        config = ConfigurationManager()
        trainer_config = config.get_model_trainer_config()
        training = ModelTrainer(trainer_config)
        training.train()