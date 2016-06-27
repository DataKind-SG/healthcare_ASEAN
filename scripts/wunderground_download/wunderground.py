import urllib2

# include your weather stations here by country, get the METARS site code from the station.txt file.
weather_stations_MY = ('WBGB','WBGG','WBGR','WBGS','WBGY','WBKK','WBKL','WBKS','WBKT','WBKW','WMAP','WMAU','WMBA','WMBT','WMKA','WMKB','WMKC','WMKD','WMKE','WMKF','WMKI','WMKJ','WMKK','WMKL','WMKM','WMKN','WMKP','WMPA','WMSA')

weather_stations_BN = ('WBSB')

weather_stations_SG = ('WSAP','WSAT','WSSL','WSSS')

weather_stations_ID = ('WAAA','WAAB','WAAP','WAAS','WAAU','WABB','WABI','WABN','WABO','WABT','WADA','WADD','WADL','WAJI','WAJJ','WAJW','WAKK','WAKT','WAMA','WAMG','WAMH','WAMI','WAML','WAMM','WAMN','WAMP','WAMR','WAMT','WAMW','WAPA','WAPH','WAPI','WAPN','WAPP','WAPR','WARR','WARS','WARQ','WASF','WASK','WASR','WASS','WIAA','WIAG','WIAM','WIAR','WIAS','WIBB','WIDD','WIHH','WIIA','WIIB','WIID','WIIH','WIII','WIIJ','WARJ','WIIK','WIIL','WIIS','WIIT','WIKB','WIKD','WIKK','WIDN','WIKN','WIKS','WIMB','WIMG','WIMM','WIMS','WIMT','WIOI','WIOK','WION','WIOO','WIOS','WIPA','WIPH','WIPK','WIPL','WIPP','WIPR','WIPT','WITA','WITC','WITM','WITT','WRBB','WAOO','WRBI','WRBK','WRBM','WRBP','WRKA','WRKC','WRKE','WRKK','WATT','WRKL','WRKM','WRKR','WRKS','WRLB','WRLG','WRLH','WRLK','WRLL','WALL','WALR','WRLR','WRLS','WRLU','WRRA','WRRB','WRRR','WRRS','WRRW','WRSJ','WRSP','WRSQ','WRSS')

weather_stations_PH = ('RPLB','RPLC','RPLI','RPLL','RPMD','RPMK','RPML','RPMP','RPMR','RPMS','RPMZ','RPUA','RPUB','RPUD','RPUH','RPUI','RPUK','RPUM','RPUN','RPUO','RPUQ','RPUR','RPUT','RPUV','RPUW','RPVA','RPVB','RPVC','RPVD','RPVF','RPVG','RPVI','RPVJ','RPVK','RPVM','RPVP','RPVR','RPVT','RPWB','RPWC','RPWE','RPWG','RPWI','RPWJ','RPWL','RPWM','RPWP','RPWS','RPWW','RPWX','RPWY','RPWZ','RPXC','RPXT','RPMT')

for year in range(2010,2016):
	# change the country you want to download meteorogical data from here
	for ws in weather_stations_PH:
		url = "https://www.wunderground.com/history/airport/{0}/{1}/1/1/CustomHistory.html?dayend=31&monthend=12&yearend={2}&format=1".format(ws, year, year)
		# and here in the folder name
		filename = "PH/{0}-{1}.csv".format(ws,year)
		response = urllib2.urlopen(url)
		with open(filename,'wb') as output:
		  output.write(response.read())
			
