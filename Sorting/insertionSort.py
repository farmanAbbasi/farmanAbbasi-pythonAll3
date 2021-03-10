###############################################################
def insertion(a):
    for i in range(1,len(a)):# i is from 1 to 4 as it will take 4 passes to sort 5 elements
        temp=a[i]
        j=i-1
        while j>=0 and temp < a[j]:# j takes 2 elemnst in first run , 3 elements in 2nd run and so on
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp
    print(a)

      
###############################################################
def swap(a,ii,jj):
    temp=a[ii]
    a[ii]=a[jj]
    a[jj]=temp
    
def minLocation(a,i):  
    loc=i
    mins=a[i]
    j=i+1
    while j<len(a):
        if(mins>a[j]):
            mins=a[j]
            loc=j
        j+=1   
    return loc

def selection(a):
    i=0
    while i<(len(a)-1):
        loc=minLocation(a,i)
        swap(a,i,loc)
        #print(a,'after swp')
        i+=1
    print(a)
####################################################################

def bubble(a):
    for i in range(0,len(a)-1):
        j=0
        while(j<len(a)-i-1):
            if a[j+1]<a[j]:
                swap(a,j,j+1)
            j+=1    
    print(a)       
               
def bsearch(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)            


bsearch([5,4,3,12,8]) 
       
a=[5,4,3,12,8]

print(a)

#insertion(a)
#selection(a)
#bubble(a)
#####################################################
a.sort()
print(a)
#####################################################
a=sorted(a)
print(a)

# note : selection sort ka best bhi O(n^2) hai lol



    
