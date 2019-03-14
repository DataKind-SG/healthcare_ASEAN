# clean SG weather data
import os.path
import sys
import pandas as pd
import logging

INPUT_DIR = '../../Data/raw/weather_SG'
OUTPUT_DIR = '../../Data/interim/weather_SG'
OUTPUT_FILE = "weekly-weather.csv"

DICT_RENAME={'Station':'location', 
             'Year':'year', 'Month':'month', 'Day':'day', 
             'Daily Rainfall Total (mm)':'Rainfall Total',
             'Highest 30 Min Rainfall (mm)':'Max 30Min Rainfall', 
             'Highest 60 Min Rainfall (mm)':'Max 60Min Rainfall',
             'Highest 120 Min Rainfall (mm)':'Max 120Min Rainfall', 
             'Mean Temperature (°C)':'Mean Temperature',
             'Maximum Temperature (°C)':'Max Temperature', 
             'Minimum Temperature (°C)':'Min Temperature',
             'Mean Wind Speed (km/h)':'Mean Wind Speed', 
             'Max Wind Speed (km/h)':'Max Wind Speed'}
COLS_RENAMED = ['location', 'year', 'week', 'month', 'day', 'Rainfall Total',
       'Max 30Min Rainfall', 'Max 60Min Rainfall',
       'Max 120Min Rainfall', 'Mean Temperature',
       'Max Temperature', 'Min Temperature',
       'Mean Wind Speed', 'Max Wind Speed']
COL_NUM = ['year', 'month', 'day', 'Rainfall Total',
       'Max 30Min Rainfall', 'Max 60Min Rainfall',
       'Max 120Min Rainfall', 'Mean Temperature',
       'Max Temperature', 'Min Temperature',
       'Mean Wind Speed', 'Max Wind Speed']
APPLY_LOGIC = {
    'Rainfall Total' : 'sum',
    'Max 30Min Rainfall' : 'max', 
    'Max 60Min Rainfall' : 'max',
    'Max 120Min Rainfall' : 'max', 
    'Mean Temperature' : 'mean',
    'Max Temperature' : 'max', 
    'Min Temperature' : 'min',
    'Mean Wind Speed' : 'mean', 
    'Max Wind Speed' : 'max'
}

logger = logging.getLogger(__name__)

def clean():
    files = os.listdir(INPUT_DIR)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    stations = [x.split('_')[0] for x in files]
    stations = list(set(stations))
    
    for station in stations:
        station_files = [x for x in files if x.startswith(station)]
        station_files.sort()
        dfWeeklyWeather = pd.DataFrame(columns=COLS_RENAMED)
        dfRemain = pd.DataFrame(columns=COLS_RENAMED)
        year = 0
        week = 0
        for filename in station_files:
            # get monthly data, read file
            file_path = os.path.join(INPUT_DIR, filename)
            dfMonth = pd.read_csv(file_path,encoding='latin1')
            dfMonth = dfMonth.rename(index=str, columns=DICT_RENAME)
            # prepare data
            for col in COL_NUM:
                dfMonth[col] = pd.to_numeric(dfMonth[col], errors='coerce')
            if dfMonth.iloc[0]['year'] != year:
                year = dfMonth.iloc[0]['year']
                week = 1
            if (len(dfRemain) > 0) and (len(dfRemain) < 7):
                dfMonth = dfRemain.append(dfMonth, ignore_index=True)
            else:
                if(len(dfRemain) > 7):
                    print(dfRemain)
            # aggregate weekly data 
            for i in range(int(len(dfMonth)/7)):
                df = dfMonth[i*7:i*7+7]
                next_idx = i*7+7
                week_data = df.agg(APPLY_LOGIC)
                week_s = pd.Series([df.iloc[0]['location'], df.iloc[0]['year'],
                                    df.iloc[0]['month'], df.iloc[0]['day'], week], 
                                   index=['location','year','month','day','week']
                                   ).append(week_data)
                dfWeeklyWeather = dfWeeklyWeather.append(week_s, ignore_index=True)
                week += 1
            dfRemain = dfMonth[next_idx:]
        out_file = station + '_' + OUTPUT_FILE 
        output_path = os.path.join(OUTPUT_DIR, out_file)
        dfWeeklyWeather.to_csv(output_path, index=False)
    

    logger.info('SG weather cleaned successfully')


if __name__ == "__main__":
    INPUT_DIR = '../../../Data/raw/weather_SG'
    OUTPUT_DIR = '../../../Data/interim/weather_SG'
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    clean()