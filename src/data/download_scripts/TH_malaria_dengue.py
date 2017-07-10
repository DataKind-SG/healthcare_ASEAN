# -*- coding: utf-8 -*-
"""Download historical RTF data from Thailand's Bureau of Epidemiology."""
from bs4 import BeautifulSoup
import re
import sys
import os
import logging
import requests

BASE_URL = 'http://www.boe.moph.go.th/boedb/surdata'
PAGE_URL = BASE_URL + '/disease.php?dcontent=old&ds={}'
DISEASE_CODES = {'Malaria': 30, 'Dengue Fever': 66}
DATA_DIR = os.path.join(os.path.abspath(__file__ + '/../../../..'), 'data/raw')

logger = logging.getLogger(__name__)


def log_url(r, *args, **kwargs):
    logger.info('Downloading %s', r.url)


def scrape_links(url):
    """Download all .rtf files linked from the given url."""
    response = requests.get(url)
    response.raise_for_status()
    logger.info('Scraping links in %s', url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.find_all(href=re.compile('.rtf'))


def format_raw_data_path(disease_subfolder, link):
    data_subfolder = link.parent.parent.find('font').contents[0].strip('()')
    file_name = link.contents[0]
    dir_path = os.path.join(DATA_DIR, disease_subfolder, data_subfolder)
    os.makedirs(dir_path, exist_ok=True)
    return os.path.join(dir_path, '%s.rtf' % (file_name))


def download_file(download_url):
    # Request will be redirected unless the HTTP referer is the original host
    headers = {'Referer': BASE_URL}
    response = requests.get(download_url, headers=headers,
                            hooks=dict(response=log_url))
    response.raise_for_status()
    return response


def download():
    # Overwrite the INFO logging level inherited from the root logger
    logging.getLogger('requests').setLevel(logging.ERROR)

    for (name, dc) in DISEASE_CODES.items():
        logger.info('Downloading files for %s', name)

        try:
            links = scrape_links(PAGE_URL.format(dc))
        except requests.exceptions.RequestException as e:
            logger.critical('Failed to GET the Bureau of Epidemiology\'s site')
            sys.exit(1)

        for index, link in enumerate(links):
            disease_subfolder = name.lower() + "_TH"
            file_path = format_raw_data_path(disease_subfolder, link)

            data_url = BASE_URL + '/' + link['href']
            try:
                raw_data = download_file(data_url)
            except requests.exceptions.RequestException as e:
                if e.response.status_code == 404:
                    logger.info('Failed to download %s since file was not found \
                    on server with HTTP status code 404', e.response.url)
                    continue
                logger.exception(
                    'Failed to download %s with HTTP status code %i',
                    e.response.url, e.response.status_code
                )
                continue

            logger.debug("Writing to %s", file_path)
            with open(file_path, 'wb') as data_file:
                data_file.write(raw_data.content)
        else:
            logger.info('Finished downloading files for %s', name)

if __name__ == '__main__':
    download()
