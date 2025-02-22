from src.datascience import logger
from src.datascience.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>>>{STAGE_NAME}<<<<<< Started!')
    dataingestion = DataIngestionTrainingPipeline()
    dataingestion.start_data_ingestion()
    logger.info(f'>>>>>{STAGE_NAME}<<<<<<< Completed!')

except Exception as e:
    logger.exception(e)
    raise e
