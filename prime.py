import math
def prime(n):
    total=0
    for i in range(1,n+1):
        count=0
        for j in range(2,int(math.sqrt(i)+1)):
            if i%j==0:
                count+=1
        if count==0:
            total+=1
            print(i,end='\n')
            
    print('total',total)        
    
def primeSteve(n):
    total=0
    arr=[1]*(n+1)
    for i in range(2,int(math.sqrt(n)+1)):
        if arr[i]==1:
            for j in range(i*i,n+1,i):
                arr[j]=0
                
    for i in range(1,n+1):
        if arr[i]==1:
            total=total+1
            print(i)
    print('total=',total)
    
    
n=10
prime(n)
primeSteve(n)

  
