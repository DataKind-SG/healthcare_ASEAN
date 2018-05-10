#This script downloads disease statistics from data.gov.sg
#download for the month.

import sys
import os
import json
import csv
import logging

logger = logging.getLogger()
logger.addHandler(logging.NullHandler())

DIRECTORY = '../../Data/raw/disease_SG'
OUTFILE = "../../Data/raw/disease_SG/weekly-dengue-malaria.csv"
DISEASE_LIST = ["Dengue Fever", "Dengue Haemorrhagic Fever", "Malaria"]

URL = 'https://data.gov.sg/api/action/datastore_search?resource_id=ef7e44f1-9b14-4680-a60a-37d2c9dda390&limit=10000'
        
def download():
    """Download disease data from data.gov.sg"""
    logger.info('Downloading raw weekly SG Dengue and Malaria data')
    
    # Python 2
    if sys.version_info < (3, 0):
        try:
            os.makedirs(DIRECTORY)
        except OSError as e:
            pass
        
        import urllib2

        request = urllib2.Request(URL, headers={'User-Agent' : "Magic Browser"})
        fileobj = urllib2.urlopen(request)
     
        temp=json.loads(fileobj.read())
        with open(OUTFILE, 'wb') as csvfile:
            logger.debug('py2: open file for writing')
            writethis = csv.writer(csvfile, delimiter=',')
            writethis.writerow(["epi_week","disease","no_of_cases"])
            for i in temp["result"]["records"]:
                if i["disease"] in DISEASE_LIST:
                    writethis.writerow([i["epi_week"], i["disease"], i["no._of_cases"]])
    # Python 3
    else:
        os.makedirs(DIRECTORY, exist_ok=True)
        import requests
    
        fileobj = requests.get(URL)
        temp=json.loads(fileobj.text)
    
        with open(OUTFILE, 'w', newline='') as csvfile:
            logger.debug('py3: open file for writing')
            writethis = csv.writer(csvfile, delimiter=',')
            writethis.writerow(["epi_week","disease","no_of_cases"])
            for i in temp["result"]["records"]:
                if i["disease"] in DISEASE_LIST:
                    writethis.writerow([i["epi_week"], i["disease"], i["no._of_cases"]])
    logger.info('Finished downloading raw SG data')
    return
    
if __name__ == '__main__':
    import logging.config
    logging.config.fileConfig('logconf.ini')
    DIRECTORY = '../../../Data/raw/disease_SG'
    OUTFILE = "../../../Data/raw/disease_SG/weekly-dengue-malaria.csv"
    download()