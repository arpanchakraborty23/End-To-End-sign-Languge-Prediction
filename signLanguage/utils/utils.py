import os,sys
import yaml
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from ensure import ensure_annotations
from signLanguage.logger.logger import logging
from signLanguage.exception.exception import CustomException

def read_yaml(file_path):
    try:
        logging.info(f' read file {file_path}')
        with open(file_path, 'r') as y:
            content=yaml.safe_load(y)
            logging.info(f"yaml file: {file_path} loaded successfully")

        return content
    except Exception as e:
        logging.info(f'error occured {str(e)}')
        raise CustomException(sys,e)
@ensure_annotations
def create_dir(path_to_directories: list, verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"created directory at: {path}")
