# This script downloads weekly disease statistics from moh.gov.sg

import os
import sys
import logging
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


DIRECTORY = '../../data/raw/disease_SG'
MOH_URL = 'https://www.moh.gov.sg'
URL = 'https://www.moh.gov.sg/resources-statistics/infectious-disease-statistics/2018/weekly-infectious-diseases-bulletin'


logger = logging.getLogger()
logger.addHandler(logging.NullHandler())


def download():
    ''' Download disease data from moh.gov.sg '''
    logger.info('Downloading raw data of SG Weekly infectious Bulletin')

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

    # Get webpage and extract the data file path
    soup = BeautifulSoup(simple_get(URL), 'html.parser')
    file_path = soup.find(lambda tag:tag.name=='a' and 'Weekly infectious bulletin' in tag.text)['href']
    data_url = MOH_URL + file_path

    try:
        # Extract data file name
        outfile = data_url[data_url.rindex('/')+1:data_url.rindex('.xlsx')+5]
        output_path = os.path.join(DIRECTORY, outfile)

        # Download raw data file
        downloader.urlretrieve(data_url, output_path)
        logger.info('Downloaded successfully to %s', os.path.abspath(output_path))

    except ValueError as e:
        logger.error('Failed extract data file name: %s', e.reason)
    except (HTTPError, URLError) as e:
        logger.error('Failed to download: %s', e.reason)


def simple_get(url):
    '''
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    '''
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        logger.error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    '''
    Returns True if the response seems to be HTML, False otherwise.
    '''
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


if __name__ == "__main__":
    import logging.config
    logging.config.fileConfig('logconf.ini')
    download()
