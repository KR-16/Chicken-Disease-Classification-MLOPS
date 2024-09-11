from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_directory: Path
    source_URL: str
    local_data_file: Path
    unzip_directory: Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_directory: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_class: int

@dataclass(frozen=True)
class PrepareCallbacksConfig:
    root_directory: Path
    tensorboard_root_log_directory: Path
    checkpoint_model_filepath: Path