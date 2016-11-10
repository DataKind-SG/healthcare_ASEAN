#This script Downloads disease statistics from data.gov.sg

import sys

OUTFILE = "out.csv"
DISEASE_LIST = ["Dengue Fever", "Dengue Haemorrhagic Fever", "Malaria"]

if sys.version_info < (3, 0):
    import urllib
    import json
    import csv
    url = 'https://data.gov.sg/api/action/datastore_search?resource_id=ef7e44f1-9b14-4680-a60a-37d2c9dda390&limit=50000'
    fileobj = urllib.urlopen(url)
    temp=json.loads(fileobj.read())


    with open(OUTFILE, 'w') as csvfile:
        writethis = csv.writer(csvfile, delimiter=' ')
        for i in temp["result"]["records"]:
            if i["disease"] in DISEASE_LIST:
                writethis.writerow([i["epi_week"], i["disease"], i["no._of_cases"]])
else:
    import urllib.request
    import json
    import csv
    url = 'https://data.gov.sg/api/action/datastore_search?resource_id=ef7e44f1-9b14-4680-a60a-37d2c9dda390&limit=50000'
    fileobj = urllib.request.urlopen(url)
    temp=json.loads(fileobj.read().decode("utf-8") )


    with open(OUTFILE, 'w') as csvfile:
        writethis = csv.writer(csvfile, delimiter=' ')
        for i in temp["result"]["records"]:
            if i["disease"] in DISEASE_LIST:
                writethis.writerow([i["epi_week"], i["disease"], i["no._of_cases"]])