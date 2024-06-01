from ChickenDiseaseClassifier.config.configuration import ConfiguationManager
from ChickenDiseaseClassifier.components.data_ingestion import DataIngestion
from ChickenDiseaseClassifier import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfiguationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>STAGE {STAGE_NAME} STARTED <<<<<<<<<")
        object = DataIngestionTrainingPipeline()
        object.main()
        logger.info(f">>>>>>>STAGE {STAGE_NAME} COMPLETED <<<<<<<<<")
    except Exception as e:
        raise e