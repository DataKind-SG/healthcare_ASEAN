from future.standard_library import install_aliases
install_aliases()

from urllib.request import urlopen
import os
import logging
import sys

data_dir = os.path.join(os.path.abspath(__file__ + '/../../../..'), 'data/raw/weather_wunderground')
logger = logging.getLogger(__name__)

# include your weather stations here by country, get the METARS site code from the station.txt file.
weather_stations_MY = ('WBGB','WBGG','WBGR','WBGS','WBGY','WBKK','WBKL','WBKS','WBKT','WBKW','WMAP','WMAU','WMBA','WMBT','WMKA','WMKB','WMKC','WMKD','WMKE','WMKF','WMKI','WMKJ','WMKK','WMKL','WMKM','WMKN','WMKP','WMPA','WMSA')

weather_stations_BN = ('WBSB')

weather_stations_SG = ('WSAP','WSAT','WSSL','WSSS')

weather_stations_ID = ('WAAA','WAAB','WAAP','WAAS','WAAU','WABB','WABI','WABN','WABO','WABT','WADA','WADD','WADL','WAJI','WAJJ','WAJW','WAKK','WAKT','WAMA','WAMG','WAMH','WAMI','WAML','WAMM','WAMN','WAMP','WAMR','WAMT','WAMW','WAPA','WAPH','WAPI','WAPN','WAPP','WAPR','WARR','WARS','WARQ','WASF','WASK','WASR','WASS','WIAA','WIAG','WIAM','WIAR','WIAS','WIBB','WIDD','WIHH','WIIA','WIIB','WIID','WIIH','WIII','WIIJ','WARJ','WIIK','WIIL','WIIS','WIIT','WIKB','WIKD','WIKK','WIDN','WIKN','WIKS','WIMB','WIMG','WIMM','WIMS','WIMT','WIOI','WIOK','WION','WIOO','WIOS','WIPA','WIPH','WIPK','WIPL','WIPP','WIPR','WIPT','WITA','WITC','WITM','WITT','WRBB','WAOO','WRBI','WRBK','WRBM','WRBP','WRKA','WRKC','WRKE','WRKK','WATT','WRKL','WRKM','WRKR','WRKS','WRLB','WRLG','WRLH','WRLK','WRLL','WALL','WALR','WRLR','WRLS','WRLU','WRRA','WRRB','WRRR','WRRS','WRRW','WRSJ','WRSP','WRSQ','WRSS')

weather_stations_PH = ('RPLB','RPLC','RPLI','RPLL','RPMD','RPMK','RPML','RPMP','RPMR','RPMS','RPMZ','RPUA','RPUB','RPUD','RPUH','RPUI','RPUK','RPUM','RPUN','RPUO','RPUQ','RPUR','RPUT','RPUV','RPUW','RPVA','RPVB','RPVC','RPVD','RPVF','RPVG','RPVI','RPVJ','RPVK','RPVM','RPVP','RPVR','RPVT','RPWB','RPWC','RPWE','RPWG','RPWI','RPWJ','RPWL','RPWM','RPWP','RPWS','RPWW','RPWX','RPWY','RPWZ','RPXC','RPXT','RPMT')


WEATHER_STATIONS = {
    'MY': weather_stations_MY,
    'BN': weather_stations_BN,
    'ID': weather_stations_ID,
    'PH': weather_stations_PH
}


def download():
    countries_to_download = ['PH', 'MY']

    for country in countries_to_download:
        for year in range(2010,2016):
            # change the country you want to download meteorogical data from here
            for ws in WEATHER_STATIONS[country]:
                logger.info(
                    "Downloading wunderground data for country %s, year %s and station %s",
                    country, year, ws
                )
                url = "https://www.wunderground.com/history/airport/{0}/{1}/1/1/CustomHistory.html?dayend=31&monthend=12&yearend={2}&format=1".format(ws, year, year)
                country_data_dir = "{}/{}".format(data_dir, country)
                # and here in the folder name
                if sys.version_info < (3, 0):
                    try:
                        os.makedirs(country_data_dir)
                    except OSError as e:
                        pass
                else:
                    os.makedirs(country_data_dir, exist_ok=True)

                filename = os.path.join(country_data_dir, "{0}-{1}.csv".format(ws,year))
                #  response = urllib2.urlopen(url)
                response = urlopen(url)
                with open(filename,'wb') as output:
                    output.write(response.read())
