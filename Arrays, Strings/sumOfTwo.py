def sumOfTwo(a,b,k):
    dict={}
    for element in a:
        dict[element]=1
    #print(dict)    
    for element in b:
        #print(dict.get(k-element))
        if dict.get(k-element):
            return True
    return False        
    
a=[0,0,-5,32022]
b=[-10,40,-3,9]
k=-8
print(sumOfTwo(a,b,k))

#O(n) time and O(n) space
    
    
