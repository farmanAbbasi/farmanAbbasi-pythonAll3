def colors(a):
    # jab 2 hai swap and j ghatao, jab 1 hai m badhao, jab 0 hai swap i and m and dono badhao
    length=len(a)
    i=0
    m=0
    j=length-1
    while m<=j:
        if(a[m]==2):
            temp=a[j]
            a[j]=a[m]
            a[m]=temp
            j=j-1
        elif a[m]==0:
            temp=a[i]
            a[i]=a[m]
            a[m]=temp
            i+=1
            m+=1
        else:
            m+=1
            
    return a        
def colors2(a):
    #jab 0 hai tabhi m badh rahe else 1 pe sirf j ghat raha bas
    m=0
    j=len(a)-1
    while m<=j:
        if(a[m]==1):
            temp=a[j]
            a[j]=a[m]
            a[m]=temp
            j-=1
        else:
            m+=1
            
    return a        
        
#print(colors2([1,1,0,0,0,1,0,1,1,1]))    
print(colors([0,2,1,2,1,1,1,1,0,0,0,2,2,2]))   
    
    
