##!/usr/bin/python3

import datetime
import sys 

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def parse(logpath):
    logfile = open(logpath, "r")
    log = logfile.read()
    ueber = log.split("\n")
    logdict = {}
    for items in ueber:
        try:
            logdict[items.split("\t")[0]] = items.split("\t")[1]
        except:
            i= 0
    return logdict

def anal(dick):
    all = len(dick)
    successfull = {}
    unsuccessfull = {}
    for key in dick:
        if dick[key] == "<Response [200]>":
            successfull[key] = dick[key]
        else:
            unsuccessfull[key] = dick[key]
    return len(unsuccessfull), len(successfull), len(unsuccessfull) / all, len(successfull) / all, unsuccessfull

def printit(perred, pergreen):
    pipe = "|"
    perred = perred * 100
    pergreen = pergreen * 100
    strred = pipe * int(perred)
    strgreen = pipe * int(pergreen)
    print(f"[{bcolors.OKGREEN}{strred}{bcolors.FAIL}{strgreen}{bcolors.ENDC}]")



logpath = "/var/log/rup/rup.log"
red, green, perred, pergreen, unsuccessfull = anal(parse(logpath))

if "--failed" in sys.argv:
    for line in unsuccessfull:
        print(line)

elif "-f" in sys.argv:
    for line in unsuccessfull:
        print(line)

elif "--help" in sys.argv:
    print("Usage: rupp [OPTION]")
    print("Parse the rup.log file to get the status of your servers uptime.")
    print(f"Arguments:")
    print(f"\t-f, --failed\t shows all uptime check fails with timestamp above the status bar.")
    print(f"\t-h, --help\t shows this help.")
    exit()

elif "-h" in sys.argv:
    print("Usage: rupp [OPTION]")
    print("Parse the rup.log file to get the status of your servers uptime.")
    print(f"Arguments:")
    print(f"\t-f, --failed\t shows all uptime check fails with timestamp above the status bar.")
    print(f"\t-h, --help\t shows this help.")
    exit()

printit(pergreen, perred)
print(f"{bcolors.OKGREEN}working uprequests \t {bcolors.OKBLUE}{green}{bcolors.ENDC}")
print(f"{bcolors.FAIL}non-working uprequests \t {bcolors.OKBLUE}{red}{bcolors.ENDC}")
