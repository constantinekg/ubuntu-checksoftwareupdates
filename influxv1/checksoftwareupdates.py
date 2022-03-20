#!/usr/bin/env python3

import time
import requests
import sys
import re
import os
import subprocess

hostname = os.uname()[1]
influxdbinitial = 'https://some.host/write?db=criticalsites'


# функция для добавления в БД influxdb инфы о обновлениях
def puttoinfluxdb(totalupdates, securityupdates):
    # заправляем инфу о кол-ве общих обновлений
    data_binary = 'softwareupdates,host='+hostname+' totalupdates='+totalupdates
    try:
        response = requests.post(influxdbinitial, data=data_binary)
        print(response)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print (e)
        sys.exit(1)
    # заправляем инфу о кол-ве обновлений на безопасность
    data_binary = 'softwareupdates,host='+hostname+' securityupdates='+securityupdates
    try:
        response = requests.post(influxdbinitial, data=data_binary)
        print(response)
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print (e)
        sys.exit(1)


def updatesnotifyget():
    #subprocess.run(["/usr/bin/apt", "update"])
    #time.sleep(3)
    f = open("/var/lib/update-notifier/updates-available", "r")
    lines = f.readlines()
    # print(lines[1]) 
    totalupdates = re.sub("[^0-9^]", "", lines[1])
    securityupdates = re.sub("[^0-9^]", "", lines[2])
    if totalupdates == '':
        totalupdates = '0'
    else:
        pass
    if securityupdates == '':
        securityupdates = '0'
    else:
        pass
    puttoinfluxdb(totalupdates, securityupdates)

if __name__ == "__main__":
    updatesnotifyget()

