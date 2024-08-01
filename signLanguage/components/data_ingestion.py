import os,sys
import gdown
import zipfile

from signLanguage.logger.logger import logging
from signLanguage.exception.exception import CustomException
from signLanguage.configuration.config_manager import ConfigManager


class DataIngestion:
    def __init__(self) -> None:
        config=ConfigManager()
        self.config=config.data_ingestion_config()

        logging.info('---------------------------- Data Ingestion Has Started --------------------------')

    def initate_data_ingestion(self):
        try:
            # download data

            # folder url
            data_url=self.config.url
            # local download folder
            local_folder=self.config.local_floder
            os.makedirs(self.config.dir,exist_ok=True)

            prefix='https://drive.google.com/uc?/export=download&id='
            id=data_url.split('/')[5]
            print(id)

            # download data
            gdown.download(prefix+id,local_folder)

            # extract zip file

            unzip_folder=self.config.unzip_floder
            with zipfile.ZipFile(local_folder,'r') as z:
                z.extractall(unzip_folder)

            logging.info('---------------------------- Data Ingestion Completed--------------------------')

        except Exception as e:
            logging.info('error occured ',str(e))
            raise CustomException(sys,e)