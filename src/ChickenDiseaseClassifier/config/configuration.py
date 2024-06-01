from ChickenDiseaseClassifier.constants import *
from ChickenDiseaseClassifier.utils.common import readYaml, createDirectories
from ChickenDiseaseClassifier.entity.config_entity import DataIngestionConfig

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