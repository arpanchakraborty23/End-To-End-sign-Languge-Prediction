import os,sys
import yaml
from signLanguage.logger.logger import logging
from signLanguage.exception.exception import CustomException

def read_yaml(file_path):
    try:
        logging.info(f' read file {file_path}')
        with open(file_path, 'r') as y:
            content=yaml.safe_load()

        return content
    except Exception as e:
        logging.info('error occured ',str(e))
        raise CustomException(sys,e)
    
def create_dir(file_path,verbose=True):
    try:
        os.makedirs(
            file_path,exist_ok=True
        )
        logging.info(f'file path {file_path} created')

    except Exception as e:
        logging.info('error occured ',str(e))
        raise CustomException(sys,e)