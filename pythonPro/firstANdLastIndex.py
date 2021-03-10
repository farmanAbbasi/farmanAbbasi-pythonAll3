def canJump(a,k):
 def helperfirst(a,k):
  ans=-1
  low=0;
  high=len(a)-1
  while low<=high:
   mid=low+(high-low)//2
   if a[mid]==k:
    ans=mid
    high=mid-1
   elif a[mid]>k:
    high=mid-1
   else:
    low=mid+1
  return ans

 def helperlast(a,k):
  ans=-1
  low=0;
  high=len(a)-1
  while low<=high:
   mid=low+(high-low)//2
   if a[mid]==k:
    ans=mid
    low=mid+1
   elif a[mid]>k:
    high=mid-1
   else:
    low=mid+1
  return ans
   
   
  


 ans=[helperfirst(a,k),helperlast(a,k)]
 return ans
 


print(canJump([2,2],2))