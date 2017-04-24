# This script downloads weekly dengue statistics from data.gov.my
import os
import sys
import logging


DIRECTORY = '../../Data/raw/disease_MY'
OUTFILE = "weekly-dengue.xlsx"
URL = "http://www.data.gov.my/data/dataset/63d41a34-f35c-4bd3-b380-c61bfb10949b/resource/bc0f93fa-f95b-4100-9d0f-a2d4c194b317/download/kesdenggi2010-2015.xlsx"

logger = logging.getLogger(__name__)


def download():

    if sys.version_info < (3, 0):
        try:
            os.makedirs(DIRECTORY)
        except OSError as e:
            pass
        import urllib as downloader
        from urllib2 import URLError, HTTPError
    else:
        os.makedirs(DIRECTORY, exist_ok=True)
        import urllib.request as downloader
        from urllib.error import URLError, HTTPError

    output_path = os.path.join(DIRECTORY, OUTFILE)

    try:
        downloader.urlretrieve(URL, output_path)
        logger.info('Downloaded successfully to %s', os.path.abspath(output_path))
    except (HTTPError, URLError) as e:
        logger.error('Failed to download: %s', e.reason)


if __name__ == "__main__":
    DIRECTORY = '../../../Data/raw/disease_MY'
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    download()