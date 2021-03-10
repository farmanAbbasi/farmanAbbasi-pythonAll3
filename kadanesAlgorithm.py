#select the current+next or next only rule
def largestSumSubarray(arr):
    localmaximum=arr[0]
    globalmaximum=localmaximum
    for i in range(1,len(arr)):
        localmaximum=max(arr[i],localmaximum+arr[i])
        if globalmaximum<localmaximum:
            globalmaximum=localmaximum
    return globalmaximum        
        
a=[-2,1,-3,4,-1,2,1,-5,4]
print(largestSumSubarray(a))
