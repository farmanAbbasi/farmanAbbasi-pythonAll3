def duplicates(A):
    B=[]
    for i in range(0,len(A)):
        if A[abs(A[i])]>0:
            A[abs(A[i])]=-1*A[abs(A[i])]
            B.append(abs(A[i])) 
        else:
            #print(abs(A[i]))# these are alternate repeating elements
            A[abs(A[i])]=A[abs(A[i])]*-1 #- se + kar diya        
    print(B)               


def kadane(A):
    max_local=-9999
    max_global=-9999
    for i in range(len(A)):
        max_local=max(A[i],max_local+A[i])
        if max_global<max_local:
            max_global=max_local
    return max_global


A=[3,1,2,5,4,5]
duplicates(A)
B=[-2,1,-3,4,-1,2,1,-5,4]
#print(kadane(B))





