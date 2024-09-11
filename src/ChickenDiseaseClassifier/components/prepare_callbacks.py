from urllib.request import urlopen
from zipfile import ZipFile
import tensorflow as tf
import time
import os
from ChickenDiseaseClassifier.entity.config_entity import PrepareCallbacksConfig
class PrepareCallback:
    def __init__(self, config:PrepareCallbacksConfig):
        self.config = config
    
    @property
    def _create_tb_callback(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_directoy = os.path.join(
            self.config.tensorboard_root_log_directory,
            f"tb_logs_at_{timestamp}"
        )
        
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_directoy)
    
    @property
    def _create_checkpoint_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath = self.config.checkpoint_model_filepath,
            save_best_only = True
        )
    
    def get_tb_checkpoint_callbacks(self):
        return [
            self._create_tb_callback,
            self._create_checkpoint_callbacks
        ]

