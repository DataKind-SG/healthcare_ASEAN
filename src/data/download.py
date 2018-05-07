# Call download scripts 
#from download import *
import download.SG_disease
import download.SG_weather
import download.MY_dengue
import download.BN_disease
import download.TH_disease
import download.ID_malaria
import download.wunderground
import download.apps_who_int
import os
import sys
import logging
import logging.config

logger = logging.getLogger()
logger.addHandler(logging.NullHandler())

DIRECTORY = '../../Data/raw'

def main():
    logger.info('Downloading raw weekly MY dengue data')
    
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    
    # Singapore
    download.SG_disease.download()
    download.SG_weather.download()

    # Brunei
    download.BN_disease.download()
    
    # Malaysia
    download.MY_dengue.download()

    #Indonesia
    download.ID_malaria.download()
    return

def temp():
    
    logger.info('Downloading raw TH data')
    download.TH_disease.download()
    logger.info('Finished downloading raw TH data')
    
    logger.info('Downloading wunderground data')
    download.wunderground.download()
    logger.info('Finished downloading wunderground data')
    
    logger.info('Downloading apps.who.int data / malaria reported confirmed cases')
    download.apps_who_int.download()
    logger.info('Finished downloading apps.who.int data / malaria reported confirmed cases')
    return


if __name__ == '__main__':
    logging.config.fileConfig('logconf.ini')
    main()
