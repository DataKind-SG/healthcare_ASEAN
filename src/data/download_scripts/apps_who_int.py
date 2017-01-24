import os
import logging
import requests

data_dir = os.path.join(os.path.abspath(__file__ + '/../../../..'), 'data/raw/apps_who_int')
try:
    os.makedirs(data_dir)
except:
    pass # directory exists

BASE_URL = "http://apps.who.int/gho/athena/data/xmart.csv"
DOWNLOAD_PARAMS = ["?target=GHO/WHS3_48&profile=crosstable&filter=COUNTRY:*&x-sideaxis=COUNTRY&x-topaxis=GHO;YEAR",
                   "?target=GHO/MALARIA002&profile=crosstable&filter=COUNTRY:*&x-sideaxis=COUNTRY&x-topaxis=GHO;YEAR",
                   "?target=GHO/MALARIA003&profile=crosstable&filter=COUNTRY:*&x-sideaxis=COUNTRY&x-topaxis=GHO;YEAR",
                   "?target=GHO/IR_INSECTICIDERESISTANCE_PREV&profile=crosstable&filter=COUNTRY:*&x-sideaxis=COUNTRY;YEAR&x-topaxis=GHO"]

FILENAMES = ["malaria-yearly-confirmed-cases.csv", "malaria-yearly-estimated-cases.csv", "malaria-yearly-estimated-deaths.csv", "malaria-yearly-overview-resistance-status.csv"]


def download():
    for (name, param) in zip(FILENAMES, DOWNLOAD_PARAMS) :
        full_url = BASE_URL+param
        r = requests.get(full_url)
        if r.ok:
            full_path = os.path.join(data_dir, name)
            with open(full_path, 'w') as f:
                f.write(r.text.encode('utf-8'))
            print("File downloaded to %s" % full_path)
        else:
            print("GET request returned status %d for url=%s" % (r.status_code, full_url))
