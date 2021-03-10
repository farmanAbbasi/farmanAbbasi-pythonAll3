def stringger(str1):
    return sorted(list(set(str1)))

str1='AAAxADD'
lst2=stringger(str1)
print(lst2)
minStr=''
minStr2=''

for i in range(len(str1)):
    if stringger(str1[i:len(str1)])==lst2:
        minStr=str1[i:len(str1)]
    else:
        break
        
for j in range(len(minStr)):
    if stringger(minStr[0:len(minStr)-j])==lst2:
        minStr2=minStr[0:len(minStr)-j]
    else:
        break
              
print(minStr2)
