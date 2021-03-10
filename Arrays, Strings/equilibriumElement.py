def pivotIndex(self, nums):
    length=len(nums)
    if length==0:
        return -1
    newnums=[0]*length
    newnums[0]=nums[0]

    for i in range(1,length):
            newnums[i]=newnums[i-1] + nums[i]
    for i in range(length):
        if(newnums[i]-nums[i]==newnums[length-1]-newnums[i]):
            return i
    return -1
       
# finding the equilibrium point
#O(n) time and O(n) space
            
            
        
