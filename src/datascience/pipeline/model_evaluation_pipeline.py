from src.datascience.config.configurations import ConfigurationManager
from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience import logger

STAGE_NAME = 'Model Evaluation Stage'

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def start_model_evaluate(self):
        config = ConfigurationManager()
        evaluate_config = config.get_model_evaluation_config()
        evaluate_model = ModelEvaluation(evaluate_config)
        evaluate_model.log_into_mlflow()
        