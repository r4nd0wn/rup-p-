#!/usr/bin/python3

import requests
import datetime
import time

logpath = "rup.log"
def pingme():
    response = requests.head('https://duckduckgo.com//')
    logfile = open(logpath, "a")
    logfile.write(str(datetime.datetime.now()) + "\t" + str(response) + "\n")
    print(response)
    logfile.close()
while True:
    pingme()
    time.sleep(30)
