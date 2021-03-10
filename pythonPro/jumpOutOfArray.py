def canJump(a):
 def helper(a,i,dp):
  if i==len(a)-1:
   return True
  if a[i]==0:
   return False
  if dp[i] != -1:
   return dp[i]
  ans=False
  for j in range(1,a[i]+1):
   ans=ans or helper(a,i+j,dp)
  dp[i]=ans
  return dp[i]

 dp=[-1]*len(a)
 return helper(a,0,dp)
 


print(canJump([1,3,2,0,2]))