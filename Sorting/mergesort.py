def mergeSort(Arr):
    if len(Arr)<2:
        return Arr
    
    mid=len(Arr)//2
    L=Arr[0:mid]
    R=Arr[mid:len(Arr)]
    #print(L,' ',R)
    L=mergeSort(L)
    R=mergeSort(R)
    return merging(L,R)
   
def merging(L,R):
    print(L,'& ',R)
    M=[]
    i=0 
    j=0 
    while(i<len(L) and j< len(R)):
        if(L[i]<R[j]):
            M.append(L[i])
            i+=1
        
        else:
            M.append(R[j])
            j+=1
           
    while(i<len(L)):
        M.append(L[i])
        i+=1
         
    while(j<len(R)):
        M.append(R[j])
        j+=1
                
    return M        
    
    
    
          


A=[20,15,35,2,4,5,11,3]
print(mergeSort(A))  
