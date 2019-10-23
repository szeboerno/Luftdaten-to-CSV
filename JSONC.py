#!/usr/bin/env python

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json, csv
def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

url = ("http://data.sensor.community/airrohr/v1/sensor/28520/")

def get_jsonparsed_data1(url2):
    response1 = urlopen(url2)
    data1 = response1.read().decode("utf-8")
    return json.loads(data1)

url2 = ("http://data.sensor.community/airrohr/v1/sensor/28519/")

list = get_jsonparsed_data(url)

list1 = list[0]

listx = get_jsonparsed_data1(url2)

listx1 = listx[0]

list_pm = [(list1["timestamp"]), list1["sensor"]["sensor_type"]["name"], list1["sensordatavalues"][0]["value_type"],
               list1["sensordatavalues"][0]["value"], list1["sensordatavalues"][1]["value_type"],
               list1["sensordatavalues"][1]["value"], (listx1["timestamp"]), listx1["sensor"]["sensor_type"]["name"],
               listx1["sensordatavalues"][0]["value_type"], listx1["sensordatavalues"][0]["value"],
               listx1["sensordatavalues"][1]["value_type"], listx1["sensordatavalues"][1]["value"]]

time1 = list1["timestamp"]
temperature = list1["sensordatavalues"][0]["value"]
humidity = list1["sensordatavalues"][1]["value"]
time2 = listx1["timestamp"]
pm10 = listx1["sensordatavalues"][0]["value"]
pm2_5 = listx1["sensordatavalues"][1]["value"]

datarow = [time1, temperature, humidity, time2, pm10, pm2_5]

with open('sensor.csv', 'a', newline='') as csv_file:
    wr = csv.writer(csv_file, dialect='excel')
    wr.writerow(datarow)
csv_file.close()
exit()









