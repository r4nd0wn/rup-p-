#!/usr/bin/python3

import datetime
import time
import os


ip = "google.com"
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
    return status
while True:
    state = pingit()
    if state == "up":
        time.sleep(30)
    elif state == "down":
        time.sleep(20)
