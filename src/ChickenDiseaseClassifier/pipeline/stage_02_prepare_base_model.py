from ChickenDiseaseClassifier.config.configuration import ConfiguationManager
from ChickenDiseaseClassifier.components.prepare_base_mode import PrepareBaseModel
from ChickenDiseaseClassifier import logger

STAGE_NAME = "PREPARE BASE MODEL STAGE"

class PrepareBaseModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfiguationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>>>>STAGE {STAGE_NAME} STARTED <<<<<<<<<<")
        object = PrepareBaseModelTrainingPipeline()
        object.main()
        logger.info(f">>>>>>>>>>STAGE {STAGE_NAME} COMPLETED <<<<<<<<<<")
    except Exception as e:
        raise e