import os.path
import sys
import pandas as pd
import logging

INPUT_DIRECTORY = '../../../data/raw/disease_SG'
INPUT_FILE = "weekly-dengue-malaria.csv"
OUTPUT_DIRECTORY = '../../../data/interim/disease_SG'
OUTPUT_FILE = "weekly-dengue-malaria-cleaned.csv"

logger = logging.getLogger(__name__)


def clean():
    input_path = os.path.join(INPUT_DIRECTORY, INPUT_FILE)
    if not os.path.isfile(input_path):
        logger.error("Input file is not found %s", os.path.abspath(input_path))
    data_frame = pd.read_csv(input_path, names=['year_week', 'disease', 'number_of_cases'])
    data_frame['country'] = 'Singapore'
    year_week = pd.DataFrame(data_frame.year_week.str.split('-').tolist(), columns=['year','week'])
    data_frame['year'] = year_week['year']
    data_frame['week'] = year_week['week'].str[1:]
    data_frame.drop('year_week', 1, inplace=True)


    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIRECTORY, OUTPUT_FILE)
    data_frame.to_csv(output_path, index=False)

    logger.info('Data clean successfully')


if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    clean()
