
import csv
from datetime import datetime


def writeToLog(filename, entry):
    with open(filename, 'a') as file:
        file.write(entry + "\n")


def readLog(filename):
    with open(filename, 'r') as file:
        return file.read()


name = input("What is your name?")
timestamp = datetime.now().strftime("%Y-%m-%d")


writeToLog('log.txt', f"{timestamp} - {name}")

print("Log Contents")
print(readLog("log.txt"))
