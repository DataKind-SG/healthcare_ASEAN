# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 12:48:12 2016

@author: Dathappy
"""

import urllib.request
import os


def download(path,month,year):
    # test of the folder name
    os.makedirs(path, exist_ok=True)
    # include your weather stations here by country, get the METARS site code from the station.txt file.
    weather_stations_SG = ('S104','S105','S109','S86','S63','S120','S55','S64','S90','S92','S61','S24','S114','S121','S11','S50','S118','S107','S39','S101','S44','S117','S33','S31','S71','S122','S566','S112','S508','S07','S40','S108','S113','S111','S119','S116','S94','S29','S06','S106','S81','S77','S25','S102','S80','S60','S36','S110','S84','S79','S43','S78','S72','S23','S88','S89','S115','S82','S35','S69','S46','S123','S91')
    # will loop thru each weather station and try to download the csv datafile
    for ws in weather_stations_SG:
        try:
            # sets the URL of the CSV
            url = "http://www.weather.gov.sg/files/dailydata/DAILYDATA_" + ws + "_"+ str(year) + str(month) + ".csv"         
            # sets the filename
            file = ws+ "_" + str(month)+str(year)+'.csv'
            filename = os.path.join(path,file)            
            # retrieve the file
            urllib.request.urlretrieve(url, filename)
        # as not all data is available the same month for all the stations you will get a 404 error if the data is not here
        except:
            pass
        
        
# set the folder name
path = r'../../Data/raw/weather_SG'

# the month seems to be the previous one ane instead of having it in the code, 
#it could be current month -1 if relevant (same for the year)
# Example: download all files of september 2016
download(path,"09","2016")