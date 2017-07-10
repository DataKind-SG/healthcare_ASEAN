import os.path
import sys
import pandas as pd
import logging

INPUT_DIRECTORY = '../../../data/raw/disease_SG'
INPUT_FILE = "weekly-dengue-malaria.csv"
OUTPUT_DIRECTORY = '../../Data/interim/disease_SG'
OUTPUT_FILE = "weekly-dengue-malaria.csv"

logger = logging.getLogger(__name__)

def clean():
    input_path = os.path.join(INPUT_DIRECTORY, INPUT_FILE)
    if not os.path.isfile(input_path):
        logger.error("Input file is not found %s", os.path.abspath(input_path))
    data_frame = pd.read_csv(input_path, names=['week', 'disease', 'number of cases'])
    print (data_frame)

    print("end")
if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    clean()