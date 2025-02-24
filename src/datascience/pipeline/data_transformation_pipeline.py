from src.datascience.components.data_transformation import DataTransformation
from src.datascience.config.configurations import ConfigurationManager
from src.datascience import logger

class DataTransformationPipeline:
    def __init__(self):
        pass

    def start_data_transformation(self):
        try:
            with open("artifacts/data_validation/status.txt", "r") as f:
                read = f.read()
                status = read.split(" ")[-1]
            if status == "True":
                config = ConfigurationManager()
                dataTransformConfig = config.get_data_transformation_config()
                datatransform = DataTransformation(dataTransformConfig)
                datatransform.transform_data()

            else:
                logger.info('Unable to Transform Data Schema Is not Valid!')
            
        except Exception as e:
            logger.info(e)
            print(e)