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
            data_ingestion.download_file()
            data_ingestion.extract_data()
           
        except Exception as e:
            logging.info('error occured ',str(e))
            raise CustomException(sys,e)
    
if __name__=='__main__':
    try:
        obj=TrainPipeline()
        obj.Pipline()

    except Exception as e:
        logging.info('error in  train pipline',str(e))
        raise CustomException(sys,e)

