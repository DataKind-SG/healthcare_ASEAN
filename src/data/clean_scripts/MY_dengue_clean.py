import os.path
import sys
import pandas as pd
import logging

INPUT_DIRECTORY = '../../Data/raw/disease_MY'
INPUT_FILE = "weekly-dengue.xlsx"
OUTPUT_DIRECTORY = '../../Data/clean/disease_MY'
OUTPUT_FILE = "weekly-dengue.csv"
ROWS_NUM = 18

logger = logging.getLogger(__name__)


def clean():

    input_path = os.path.join(INPUT_DIRECTORY, INPUT_FILE)
    if not os.path.isfile(input_path):
        logger.error("Input file is not found %s", os.path.abspath(input_path))

    frames = []
    skiprows = 1
    skip_footer = 110
    for year in ['2010', '2011', '2012', '2013', '2014']:
        df = pd.read_excel(input_path, na_values="na", skiprows=skiprows, skip_footer=skip_footer, parse_cols=52, index=False)

        df = pd.melt(df, var_name='week_num', value_name='cases', id_vars='NEGERI').set_index('NEGERI')
        df['year'] = year
        df['week_num'] = df['week_num'].map(lambda x: x.strip()).str[-2:].astype(int)
        df = df.reset_index()
        df.rename(columns={'NEGERI': 'region', 'week_num': 'week'}, inplace=True)

        frames.append(df)

        skiprows += ROWS_NUM
        skip_footer -= ROWS_NUM

    df = pd.concat(frames)

    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIRECTORY, OUTPUT_FILE)
    df.to_csv(output_path, index=False)


if __name__ == "__main__":
    INPUT_DIRECTORY = '../../../Data/raw/disease_MY'
    OUTPUT_DIRECTORY = '../../../Data/clean/disease_MY'
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    clean()