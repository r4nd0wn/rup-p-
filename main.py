#!/usr/bin/python3

import datetime
import time
import os


ip = "8.8.8.8"
logpath = "/var/log/rup/rup.log"
status = ""
def pingit():
    pings = os.system("ping -c 1 " + ip)
    if pings == 0:
        status = "up"
    else:
        status = "down"

    logfile = open(logpath, "a")
    logfile.write(str(datetime.datetime.now()) + "\t" + status + "\n")
    print(status)
    logfile.close()
while True:
    pingit()
    time.sleep(30)
