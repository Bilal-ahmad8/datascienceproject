from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.data_validation_pipeline import DataValidationPipeline


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