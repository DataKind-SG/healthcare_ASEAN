# This script downloads yearly malaria statistics from data.go.id
# It uses urllib and is compatible with both Python 2 and 3

import os
import sys
import logging #logs what goes on

DIRECTORY = '../../data/raw/disease_ID'
OUTFILE = "yearly-malaria.csv"
OUTFILE2015 = "malaria-2015.xlsx"
URL = "http://data.go.id/dataset/cef9b348-91a9-4270-be1d-3cf64eb9d5b0/resource/42f31bb0-af59-4c96-9a74-db3283f9e316/download/kasusmalaria.csv"
URL2015 = "http://data.go.id/dataset/cef9b348-91a9-4270-be1d-3cf64eb9d5b0/resource/2965b760-0f7f-4bd7-9dbe-8d261729e12f/download/jumlahkasusangkakesakitanmalariaper1000pendudukberisiko.xlsx"

logger = logging.getLogger()
logger.addHandler(logging.NullHandler())

def download():
    """ Download malaria statistics from data.go.id """
    logger.info("Downloading raw data of Malaria statistics in Indonesia between 2010 - 2015")

    # compatibility check between python 2 and 3
    if sys.version_info < (3, 0):
        # for python 2, use this
        try:
            os.makedirs(DIRECTORY)
        except OSError as e:
            pass
        import urllib as downloader
        from urllib2 import URLError, HTTPError
    else:
        # for python 3, use this
        os.makedirs(DIRECTORY, exist_ok=True)
        import urllib.request as downloader
        from urllib.error import URLError, HTTPError

    output_path = os.path.join(DIRECTORY, OUTFILE)
    output_path_2015 = os.path.join(DIRECTORY, OUTFILE2015)

    # now retrieve the file
    try:
        downloader.urlretrieve(URL, output_path)
        logger.info('Downloaded yearly stats successfully to %s', os.path.abspath(output_path))

        downloader.urlretrieve(URL2015, output_path_2015)
        logger.info('Downloaded 2015 stats successfully to %s', os.path.abspath(output_path_2015))
    except (HTTPError, URLError) as e:
        logger.error('Failed to download: %s', e.reason)


if __name__ == "__main__":
    import logging.config
    logging.config.fileConfig('logconf.ini')
    DIRECTORY = '../../../data/raw/disease_ID'
    download()
