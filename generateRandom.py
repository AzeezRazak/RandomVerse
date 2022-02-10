from random import randint
import datetime, time, pytz
import csv
import pandas as pd
import random

# datetime.now(pytz.timezone('Asia/Singapore')).strftime("%m-%d-%Y %H:%M:%S")

def generateInteger():
    value = randint(0,100)
    return(value)

def generateRandomChoice():
    choice = ["+", "N", "-"]
    return(choice)

def generateNow():
    now1 = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    return(now1)
"""
def generateSgNow():
    now2 = datetime.datetime.now(pytz.timezone('Asia/Singapore')).strftime("%m-%d-%Y %H:%M:%S")
    return(now2)
"""

def main():
    df = pd.DataFrame({
        "time": generateNow(),
        #"sgtime": generateSgNow(),
        "intVar1": [generateInteger()],
        "intVar2": [generateInteger()],
        "intVar3": [generateInteger()],
        "intVar4": [generateInteger()],
        })
    df.to_csv('Names.csv', index=False)
    time.sleep(5)

    while(1):
        df1 = pd.DataFrame({
        "time": generateNow(),
        #"sgtime": generateSgNow(),
        "intVar1": [generateInteger()],
        "intVar2": [generateInteger()],
        "intVar3": [generateInteger()],
        "intVar4": [generateInteger()],
        })
        df1.to_csv('Names.csv', mode='a', header=False, index=False)
        time.sleep(15)

if __name__ == "__main__":
    main()


