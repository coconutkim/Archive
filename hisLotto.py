from random import *

def oneline():
    lnum = set([])
    while True:
        lnum.add(int(random()*45)+1)
        if len(lnum)==6:
            break
    print(sorted(lnum))

lottoCnt = input("how many do you need? ")

for i in range(int(lottoCnt)):
    oneline()