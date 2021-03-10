
import math
import os
import random
import re
import sys

# Complete the getWays function below.
def getWays(n, c):
    amount=n
    combinations=[0]*(n+1)
    combinations[0]=1
    for coin in c:
        for i in range(len(combinations)):
            if(i>=coin):
                combinations[i]=combinations[i]+combinations[i-coin]
    
    return combinations[amount]


if __name__ == '__main__':
    nm = input().split()

    whatSum = int(nm[0])

    howManyCoins = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(whatSum, c)
    print(ways)

