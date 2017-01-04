import os
import logging
import requests

data_dir = os.path.join(os.path.abspath(__file__ + '/../../../..'), 'data/raw/apps_who_int')
try:
    os.makedirs(data_dir)
except:
    pass # directory exists

DOWNLOAD_URL = "http://apps.who.int/gho/athena/data/xmart.csv?target=GHO/WHS3_48&profile=crosstable&filter=COUNTRY:*&x-sideaxis=COUNTRY&x-topaxis=GHO;YEAR"
OUTPUT = os.path.join(data_dir, "malaria-yearly-confirmed-cases.csv")


def download():
    r = requests.get(DOWNLOAD_URL)    
    if r.ok:
        with open(OUTPUT, 'w') as f:
            f.write(r.text.encode('utf-8'))
        print("File downloaded to %s" % OUTPUT)
    else:
        print("GET request returned status %d for url=%s" % (r.status_code, DOWNLOAD_URL))
