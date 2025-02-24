from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationPipeline
from src.datascience.pipeline.data_transformation_pipeline import DataTransformationPipeline

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