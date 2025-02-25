from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.datascience.pipeline.model_trainer_pipeline import ModelTrainerPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>>>{STAGE_NAME}<<<<<< Started!')
    dataingestion = DataIngestionTrainingPipeline()
    dataingestion.start_data_ingestion()
    logger.info(f'>>>>>{STAGE_NAME}<<<<<<< Completed!')

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f'>>>>>>{STAGE_NAME}<<<<<< Started!')
    data_validation = DataValidationPipeline()
    data_validation.start_data_validation()
    logger.info(f'>>>>>>>{STAGE_NAME}<<<<<<< Completed!')

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f'>>>>>>{STAGE_NAME}<<<<<< Started!')
    data_transform = DataTransformationPipeline()
    data_transform.start_data_transformation()
    logger.info(f'>>>>>>>{STAGE_NAME}<<<<<<< Completed!')

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Model Trainer Stage'
try:
    logger.info(f'>>>>>>{STAGE_NAME}<<<<<< Started!')
    model_trainer = ModelTrainerPipeline()
    model_trainer.start_model_training()
    logger.info(f'>>>>>>>{STAGE_NAME}<<<<<<< Completed!')

except Exception as e:
    logger.exception(e)
    raise e