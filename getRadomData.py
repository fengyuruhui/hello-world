#!/usr/bin/python

import random


"""
generate radom numbers for sorting.
"""

def getRadomData(amount):
    randData = []
    i = 0
    while i < amount:
        randData.append(random.randint(0, 100))
        i += 1
    
    return randData


if __name__ == "__main__":
    amount = 20
    print getRadomData(amount)