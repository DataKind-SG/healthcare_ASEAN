import urllib
import json
import csv
url = 'https://data.gov.sg/api/action/datastore_search?resource_id=ef7e44f1-9b14-4680-a60a-37d2c9dda390&limit=50000'
fileobj = urllib.urlopen(url)
temp=json.loads(fileobj.read())


with open('out.csv', 'wb') as csvfile:
    writethis = csv.writer(csvfile, delimiter=' ')
    for i in temp["result"]["records"]:
        if i["disease"]=="Dengue Fever" or i["disease"]=="Dengue Haemorrhagic Fever" or i["disease"]=="Malaria":
            writethis.writerow([i["epi_week"], i["disease"], i["no._of_cases"]])