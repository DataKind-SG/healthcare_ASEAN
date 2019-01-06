# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 12:48:12 2016
@author: Dathappy
Modified: 5 May 2018 by arynchoong
"""

import os
import urllib.request as r
import pandas as pd
from datetime import datetime
import logging

DIRECTORY = '../../Data/raw/'

logger = logging.getLogger()
logger.addHandler(logging.NullHandler())

def download():
    """Download weather data from weather.gov.sg"""
    logger.info('Downloading weather data from weather.gov.sg')

    # test of the folder name
    base_url = "http://www.weather.gov.sg/files/dailydata/DAILYDATA_"
    out_path = DIRECTORY + "weather_SG/"
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    # weather stations that has data from year 2012 onwards, and has mean teamperatures.
    # http://www.weather.gov.sg/wp-content/uploads/2016/12/Station_Records.pdf
    weather_station_ids = [23, 24, 25, 43, 44, 50, 60, 80, 86, 102, 104, 106, 107, 108, 109, 111, 115]
    current_year = int(datetime.today().strftime("%Y"))
    today_ym = int(datetime.today().strftime("%Y%m"))
    today_d = int(datetime.today().strftime("%d"))
    logger.debug('today ym: %d, day %d', today_ym, today_d)

    # add headers by building an opener
    opener = r.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    # will loop thru each weather station and try to download the csv datafile
    for year in range(2012,current_year+1):
        y = str(year)
        for month in range(1,13):
            m = "%02d"%month
            file_ym = int(y+m)
            if ((file_ym == (today_ym-1)) and (today_d <= 10)):
                break
            elif (file_ym == today_ym):
                break
            for station_id in weather_station_ids:
                ws = 'S' + str(station_id)
                try:
                    # set URL
                    url = base_url + ws + "_" + y + m + ".csv"
                    # set out file name
                    filename = out_path + ws + "_" + y + m + ".csv"
                    # Download the file from `URL` and save it locally under `FILE_NAME`:
                    with opener.open(url) as response:
                        if response.getcode() == 200:
                            with open(filename, 'wb') as out_file:
                                data = response.read() # a `bytes` object
                                out_file.write(data)
                except:
                    # as not all data is available the same month for all the stations you will get a 404 error if the data is not here
                    logger.debug('error, url: %s',url)
                    pass

if __name__ == '__main__':
    import logging.config
    logging.config.fileConfig('logconf.ini')
    DIRECTORY = '../../../Data/raw/'
    download()

# TODO:
# the month seems to be the previous one ane instead of having it in the code,
#it could be current month -1 if relevant (same for the year)
# Example: download all files of september 2016
