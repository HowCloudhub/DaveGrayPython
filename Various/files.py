
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

x = input("What is the value of x? ")
y = input('What is the value of y? ')
z = input('What is the value of z? ')

if x < y:
    print(f'{x} is more than {y}')

if x > y:
    print(f'{x} is less than {y}')

if x > y:
    if y < z:
        print(f"While {x} is more than {y}, {y} is less than {z}")
