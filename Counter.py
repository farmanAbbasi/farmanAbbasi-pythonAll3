from collections import Counter
elements=['a','c','b','b','c','c','a']

print(Counter(elements))
#or
print(elements)
dicter={}
for element in elements:
    if element in dicter:
        dicter[element]+=1
    else:
        dicter[element]=1
        
print(dicter)


