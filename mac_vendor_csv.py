import requests
import time
import datetime


with open('macaddresslist.txt') as f:
    macaddresslist = f.read().splitlines()

for addr in macaddresslist:
    now = datetime.datetime.now()
    date_time = now.strftime ("%D/%M/%Y %H:%M:%S")
    vendor = requests.get('http://api.macvendors.com/' + addr).text
    print(addr, vendor)
    time.sleep(1)

