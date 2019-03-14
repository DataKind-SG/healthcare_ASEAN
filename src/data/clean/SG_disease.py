# src/data/clean/SG_disease.py

import os.path
import sys
import pandas as pd
import logging

INPUT_DIRECTORY = '../../data/raw/disease_SG'
INPUT_FILE = 'weekly-infectious-bulletin_caseswk09y2019.xlsx'
OUTPUT_DIRECTORY = '../../data/interim/disease_SG'
OUTPUT_FILE = "weekly-dengue-malaria-cleaned.csv"

logger = logging.getLogger(__name__)


def clean():
    input_path = os.path.join(INPUT_DIRECTORY, INPUT_FILE)
    if not os.path.isfile(input_path):
        logger.error("Input file is not found %s", os.path.abspath(input_path))
        return
    od_disease = pd.read_excel(input_path, sheet_name=None, na_values="na", skiprows=1)
    
    # collate data from spreadsheets
    df_disease = pd.DataFrame()
    for key, value in od_disease.items():
        year = int(key.split()[1])
        if 'DHF' in value.columns:
            df = value[['Epidemiology Wk', 'Dengue ', 'DHF', 'Malaria']]
        else:
            df = value[['Epidemiology Wk', 'Dengue Fever', 'Dengue Haemorrhagic Fever', 'Malaria']]
            df = df.rename(index=str, columns={"Dengue Fever": "Dengue ", "Dengue Haemorrhagic Fever": "DHF"})
        df.dropna(thresh=3, inplace=True)
        df['year'] = year
        df_disease = pd.concat([df_disease,df], ignore_index=True)
    
    # rename columns, clean
    df_disease.rename(str.strip, axis='columns', inplace=True)
    df_disease.rename(index=str, columns={"Epidemiology Wk": "week"}, inplace=True)
    df_disease.fillna(0, inplace=True)
    df_disease = df_disease.applymap(lambda x: int(x))
    df_disease['Dengue'] = df_disease['Dengue'] + df_disease['DHF']
    df_disease.drop('DHF', axis=1, inplace=True)
    df_disease = df_disease[['year', 'week', 'Dengue', 'Malaria']]


    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIRECTORY, OUTPUT_FILE)
    df_disease.to_csv(output_path, index=False)

    logger.info('Data clean successfully')


if __name__ == "__main__":
    INPUT_DIRECTORY = '../../../data/raw/disease_SG'
    OUTPUT_DIRECTORY = '../../../data/interim/disease_SG'
    logging.basicConfig(level=logging.DEBUG)
    clean()
