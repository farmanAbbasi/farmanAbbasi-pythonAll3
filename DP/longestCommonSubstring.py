#the only difference between subsequence and this is this has to return the maximum value from the DP table
    def findLength(self, A, B):
        l1=len(A)
        l2=len(B)
        listy=[[0 for x in range(l1+1)] for y in range(l2+1)]
        
        for i in range(l2):
            for j in range(l1):
                if A[j]==B[i]:
                    listy[i][j]=1+listy[i-1][j-1]
                else:
                    listy[i][j]=0
        maxi=-9999            
        for i in range(l2):
            for j in range(l1): 
                if  maxi<listy[i][j]:
                    maxi=listy[i][j]
                
        return maxi

#recurisve
        def findLength(self, A, B):
        l1=len(A)
        l2=len(B)
        count=0
        return self.helper(A,B,l1,l2,count)
        
    def helper(self,A,B,l1,l2,count):
        if l1==0 or l2==0:
            return count
        ans=0
        if A[l1-1]==B[l2-1]:
            count=self.helper(A,B,l1-1,l2-1,count+1)
        #note its not in else its calculated always
        count= max(count,max(self.helper(A,B,l1-1,l2,0),self.helper(A,B,l1,l2-1,0))) 
        return count  
      
        
