from signLanguage.components.data_ingestion import DataIngestion
from signLanguage.configuration.config_manager import ConfigManager

from signLanguage.exception.exception import CustomException
from signLanguage.logger.logger import logging

import os,sys

class TrainPipeline:
    def __init__(self) -> None:
        logging.info('************* Traning Pipline *************')

    def Pipline(self):
        try:
            data_ingestion=DataIngestion()
            data_ingestion.initate_data_ingestion()
        except Exception as e:
            logging.info('error occured ',str(e))
            raise CustomException(sys,e)