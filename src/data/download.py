# Call download scripts 
from download import *
import os

import logging
logger = logging.getLogger(__name__)
log.addhandler(logging.NullHandler())

DIRECTORY = '../../Data/raw'

def main():
    logger.info('Downloading raw weekly MY dengue data')
    
    if sys.version_info < (3, 0):
        if not os.path.exists(DIRECTORY):
            os.makedirs(DIRECTORY)
    else:
        os.makedirs(DIRECTORY, exist_ok=True)
    
    # Singapore
    download.SG_disease_down.download()
    download.SG_weather.download()
    
    logger.info('Downloading raw weekly MY dengue data')
    download.MY_dengue_down.download()
    logger.info('Finished downloading raw MY data')
    
    logger.info('Downloading raw weekly BN dengue data')
    download.BN_dengue_malaria.download()
    logger.info('Finished downloading raw BN data')
    
    logger.info('Downloading raw TH data')
    download.TH_malaria_dengue.download()
    logger.info('Finished downloading raw TH data')
    
    logger.info('Downloading wunderground data')
    download.wunderground.download()
    logger.info('Finished downloading wunderground data')
    
    logger.info('Downloading apps.who.int data / malaria reported confirmed cases')
    download.apps_who_int.download()
    logger.info('Finished downloading apps.who.int data / malaria reported confirmed cases')


if __name__ == '__main__':
    main()
