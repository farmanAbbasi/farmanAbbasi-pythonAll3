#the array elements can be within size of the array inclusive
def secondOccurence(arr):
    for i in range(len(arr)):
        if arr[abs(arr[i])-1]<0:
            return abs(arr[i])

        else:
            arr[abs(arr[i])-1]=-1*arr[abs(arr[i])-1]
    return -1        
        


arr=[3,1,3,4,2]
print(secondOccurence(arr))
