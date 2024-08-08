import os,sys
import zipfile
import requests

import gdown
from signLanguage.logger.logger import logging
from signLanguage.exception.exception import CustomException
from signLanguage.configuration.config_manager import ConfigManager
from signLanguage.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self) -> None:
        config=ConfigManager()
        self.config=config.data_ingestion_config()



    def download_file(self):
        try:
            logging.info('<---------------- Data Ingestion ---------------->')

            # geting data url
            dataset_url=self.config.url

            # create a local data folder
            os.makedirs(self.config.dir,exist_ok=True)


            # download data in local folder
            local_floder=self.config.local_floder

            # unzip data
            unzip_data=self.config.unzip_floder
           
            zip_data=requests.get(dataset_url)

            # save to local folder
            with open(local_floder,'wb') as l:
                l.write(zip_data.content)


            print(f"File downloaded successfully and saved to {local_floder}")
            logging.info('Zip data download completed')

      
        except Exception as e:
            logging.info(f' Error occured {str(e)}')
            raise CustomException(sys,e)
        
    def extract_data(self):
        try:
            unzip_dir=self.config.unzip_floder
            local_floder=self.config.local_floder

            # extract zip folder
            with zipfile.ZipFile(local_floder,'r') as zip:
                zip.extractall(unzip_dir)

            logging.info('data extracted')

            logging.info('<---------------- Data Ingestion Completed ---------------->')

        except Exception as e:
            logging.info(f'error extract file {e}')
            raise CustomException(sys,e)
        

    