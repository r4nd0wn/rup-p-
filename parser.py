#!/usr/bin/python3

import datetime
import sys 
import os

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
        if dick[key] == "up":
            successfull[key] = dick[key]
        else:
            unsuccessfull[key] = dick[key]
    return len(unsuccessfull), len(successfull), len(unsuccessfull) / all, len(successfull) / all, unsuccessfull, dick

def printit(perred, pergreen, cols):
    cols = cols - 2
    pipe = "|"
    strred = pipe * round(cols * perred)
    strgreen = pipe * round(cols * pergreen)
    print(f"[{bcolors.OKGREEN}{strred}{bcolors.FAIL}{strgreen}{bcolors.ENDC}]")

def estimateTimes(unsucc, succ):
    secsucc = succ * 30
    secunsucc = unsucc * 30
    timedsucc = datetime.timedelta(seconds=secsucc)
    timedunsucc = datetime.timedelta(seconds=secunsucc)
    return timedunsucc, timedsucc



logpath = "/var/log/rup/rup.log"
red, green, perred, pergreen, unsuccessfull, allcalls = anal(parse(logpath))
timered, timegreen = estimateTimes(red, green)
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
cols, rows = os.get_terminal_size(0)
printit(pergreen, perred, cols)
print(f"{bcolors.OKGREEN}working uprequests \t {bcolors.OKBLUE}{green}{bcolors.ENDC}")
print(f"{bcolors.OKGREEN}estimated time online \t {bcolors.OKBLUE}{timegreen}{bcolors.ENDC}")
print(f"{bcolors.FAIL}non-working uprequests \t {bcolors.OKBLUE}{red}{bcolors.ENDC}")
print(f"{bcolors.FAIL}estimated time offline \t {bcolors.OKBLUE}{timered}{bcolors.ENDC}")
