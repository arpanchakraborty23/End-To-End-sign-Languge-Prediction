from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    dir: Path
    url: Path
    local_floder: Path
    unzip_floder: Path