from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_directory: Path
    source_URL: str
    local_data_file: Path
    unzip_directory: Path