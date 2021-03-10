def longestCommonSubsequence(self, str1, str2):
       l1=len(str1)
       l2=len(str2)
       listy = [[0 for x in range(l1+1)] for y in range(l2+1)]
       #print(listy)
       for i in range(1,l2+1):
              for j in range(1,l1+1):
                     if(str2[i-1]==str1[j-1]):
                            listy[i][j]=listy[i-1][j-1]+1
                     else:
                           listy[i][j]=max(listy[i][j-1],listy[i-1][j])
       #print(listy)            
       return listy[l2][l1]

#recursive fails due to time limit
#     def longestCommonSubsequence(self, str1: str, str2: str) -> int:
#         l1=len(str1)
#         l2=len(str2)
        
#         return self.helper(str1,str2,l1,l2)
    
#     def helper(self,str1,str2,l1,l2):
#         if l1==0 or l2==0:
#             return 0
#         if str1[l1-1]==str2[l2-1]:
#             return 1+ self.helper(str1,str2,l1-1,l2-1)
#         else:
#             return max(self.helper(str1,str2,l1-1,l2),self.helper(str1,str2,l1,l2-1))
#memoization
#only difference is return if u have  else store and then return
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
        l1=len(str1)
        l2=len(str2)
        listy=[[-1 for x in range(l2)] for y in range(l1)]
        return self.helper(str1,str2,l1,l2,listy)
    
    def helper(self,str1,str2,l1,l2,listy):
        if l1==0 or l2==0:
            return 0
        if listy[l1-1][l2-1]!=-1:
            return listy[l1-1][l2-1]
        
        if str1[l1-1]==str2[l2-1]:
            listy[l1-1][l2-1]= 1+ self.helper(str1,str2,l1-1,l2-1,listy)
            return listy[l1-1][l2-1]
        else:
            listy[l1-1][l2-1]= max(self.helper(str1,str2,l1-1,l2,listy),self.helper(str1,str2,l1,l2-1,listy))
            return listy[l1-1][l2-1]
        
