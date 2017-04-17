# -*- coding: utf-8 -*-
import click
import logging
import download_scripts.SG_disease_down
import download_scripts.TH_malaria_dengue
import download_scripts.wunderground
import download_scripts.MY_dengue_down
import os

def validate_log_level(ctx, param, value):
    try:
        value = getattr(logging, value.upper())
    except AttributeError as e:
        raise click.BadParameter(
            'must be one of [info|debug|warning|error|critical]')
    return value

DIRECTORY = '../../Data/raw'

@click.command()
@click.option('--log', default='warning', callback=validate_log_level, help='Set logger level')

def main(log):
    #os.makedirs(DIRECTORY, exist_ok=True)
    
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(format=log_fmt, level=log)
    logger = logging.getLogger(__name__)
    
    logger.info('Downloading raw weekly SG Dengue and Malaria data')
    download_scripts.SG_disease_down.download()
    logger.info('Finished downloading raw SG data')

#    logger.info('Downloading raw weekly MY dengue data')
#    download_scripts.MY_dengue_down.download()
#    logger.info('Finished downloading raw MY data')
#    
#    logger.info('Downloading raw TH data')
##    download_scripts.TH_malaria_dengue.download()
#    logger.info('Finished downloading raw TH data')
#    
#    logger.info('Downloading wunderground data')
#    #py3
#    download_scripts.wunderground.download()
#    logger.info('Finished downloading wunderground data')
#    
#    logger.info('Downloading apps.who.int data / malaria reported confirmed cases')
##    download_scripts.apps_who_int.download()
#    logger.info('Finished downloading apps.who.int data / malaria reported confirmed cases')
if __name__ == '__main__':
    main()
