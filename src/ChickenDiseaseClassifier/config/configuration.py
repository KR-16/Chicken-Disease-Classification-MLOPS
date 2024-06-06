from ChickenDiseaseClassifier.constants import *
from ChickenDiseaseClassifier.utils.common import readYaml, createDirectories
from ChickenDiseaseClassifier.entity.config_entity import (DataIngestionConfig, PrepareBaseModelConfig)

class ConfiguationManager:

    """
    All these values are taken from the config file
    """
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = PARAMS_FILE_PATH
            ):
        
        self.config = readYaml(config_filepath)
        self.params = readYaml(params_filepath)

        createDirectories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
         config = self.config.data_ingestion
         createDirectories([config.root_directory])

         data_ingestion_config = DataIngestionConfig(
             root_directory = config.root_directory,
             source_URL = config.source_URL,
             local_data_file = config.local_data_file,
             unzip_directory = config.unzip_directory
            )
         
         return data_ingestion_config
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        createDirectories([config.root_directory])

        prepare_base_mode_config = PrepareBaseModelConfig(
            root_directory=Path(config.root_directory),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_class=self.params.CLASSES,
            params_learning_rate=self.params.LEARNING_RATE
        )
        return prepare_base_mode_config