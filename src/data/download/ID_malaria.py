# This script downloads yearly malaria statistics from data.go.id
# It uses urllib and is compatible with both Python 2 and 3

import os
import sys
import logging #logs what goes on

DIRECTORY = '../../Data/raw/disease_ID'
OUTFILE = "yearly-malaria.csv"
URL = "http://data.go.id/dataset/cef9b348-91a9-4270-be1d-3cf64eb9d5b0/resource/42f31bb0-af59-4c96-9a74-db3283f9e316/download/kasusmalaria.csv"
URL2015 = "http://data.go.id/dataset/cef9b348-91a9-4270-be1d-3cf64eb9d5b0/resource/2965b760-0f7f-4bd7-9dbe-8d261729e12f/download/jumlahkasusangkakesakitanmalariaper1000pendudukberisiko.xlsx"
logger = logging.getLogger(__name__)


def download():
    
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

# now retrieve the file
try:
    downloader.urlretrieve(URL, output_path)
        logger.info('Downloaded successfully to %s', os.path.abspath(output_path))
    except (HTTPError, URLError) as e:
        logger.error('Failed to download: %s', e.reason)


if __name__ == "__main__":
    DIRECTORY = '../../../Data/raw/disease_ID'
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    download()
