def coin(coins,m):
    combinations=[0]*(m+1)
    combinations[0]=1
    for coin in coins:
        for i in range(1,len(combinations)):
            if i>=coin:
                combinations[i]=combinations[i-coin]+combinations[i]
    return combinations[m]
a=[1,3,5,7]
m=8
print(coin(a,m))
