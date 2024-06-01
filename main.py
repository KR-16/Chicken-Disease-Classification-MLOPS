from ChickenDiseaseClassifier import logger
from ChickenDiseaseClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>STAGE {STAGE_NAME} STARTED <<<<<<<<<")
        object = DataIngestionTrainingPipeline()
        object.main()
        logger.info(f">>>>>>>STAGE {STAGE_NAME} COMPLETED <<<<<<<<<")
    except Exception as e:
        raise e