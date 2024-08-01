import os,sys

from signLanguage.entity.config_entity import DataIngestionConfig
from signLanguage.constant.ymal_path import *
from signLanguage.logger.logger import logging
from signLanguage.exception.exception import CustomException
from signLanguage.utils.utils import read_yaml,create_dir

class ConfigManager:
    def __init__(self,config_file_path=config_file) -> None:
        self.config=read_yaml(config_file_path)

        create_dir(self.config.artifats_root)

    def data_ingestion_config(self):
        try:
            config=self.config.Data_Ingestion
            create_dir(config.dir)

            data_ingestion_config=DataIngestionConfig(
                dir=config.dir,
                url=config.url,
                local_floder=config.local_folder,
                unzip_floder=config.unzip_folder
            )

            return data_ingestion_config
        
        except Exception as e:
            logging.info('error occured ',str(e))
            raise CustomException(sys,e)