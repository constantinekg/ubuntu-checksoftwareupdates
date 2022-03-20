#!/usr/bin/env python3

from datetime import datetime
import re
import os
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# You can generate an API token from the "API Tokens Tab" in the UI
token = "DKEbHRs_9LgpG1yaFXrBSOI1TZhhkaHPvWFfH0ClgJxDHy-hUBajhskrnbweiuiqwqFJvyO2bVeM9WODNxw7i_3dQ==" # generate token in influxdb
org = "BIG ORG LLC" # organization name
bucket = "ubuntu-server-updates" # name of bucket
dbinitialurl = 'http://someurl.tld:8086' # influxdb initial url
hostname = os.uname()[1]

def puttoinfluxdb(totalupdates, securityupdates):
    with InfluxDBClient(url=dbinitialurl, token=token, org=org) as client:
        write_api = client.write_api(write_options=SYNCHRONOUS)
        data = "softwareupdates,host=" + hostname + " totalupdates=" + totalupdates
        write_api.write(bucket, org, data)
        data = "softwareupdates,host=" + hostname + " securityupdates=" + securityupdates
        write_api.write(bucket, org, data)
        client.close()

def updatesnotifyget():
    f = open("/var/lib/update-notifier/updates-available", "r")
    lines = f.readlines()
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
    print ('Total updates: ' + str(totalupdates))
    print ('Sucurity updates: ' + str(securityupdates))
    print ('Writing data into influx...')
    puttoinfluxdb(totalupdates, securityupdates)


if __name__ == '__main__':
    updatesnotifyget()

