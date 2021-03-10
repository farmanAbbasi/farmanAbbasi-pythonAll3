#his s for largest substring and also its length
def largestSubstring(s1,s2):
    result=''
    maxi=-99999
    l1=len(s1)
    l2=len(s2)
    result2=''
    matrix = [[0]*l2 for i in range(l1)]
    #print(matrix)
    for i in range(l1):
        for j in range(l2):
            if s1[i]==s2[j]:
                if i==0 or j==0:
                    matrix[i][j]=1
                else:
                    matrix[i][j]=matrix[i-1][j-1]+1
                result2=result   
                if(maxi<matrix[i][j]):
                    result=''
                    maxi=matrix[i][j]
                    result=s1[i-maxi+1:i+1]
                elif maxi==matrix[i][j]:
                    result=result+' '+s1[i-maxi+1:i+1]#ye main hai as agar teen hai maxi ki value so teen matches hain so teen peeche aake lo value
                
            '''
            #add this for getting len of largest common subsequence
            else:
                matrix[i][j]=max(matrix[i-1][j],matrix[i][j-1])

            '''   
                        
    return result


if __name__=='__main__':
    s1='harlry'
    s2='salry'
    result=largestSubstring(s1,s2)
    print(result)

'''
largest common subsequence
def lcs(X, Y, m, n): 
  
    if m == 0 or n == 0: 
       return 0
    elif X[m-1] == Y[n-1]: 
       return 1 + lcs(X, Y, m-1, n-1)
    else: 
       return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n)) 
  
  
# Driver program to test the above function 
X = [1,45,7,3,65,8]
Y = sorted(X)
print("Length of LCS is ", lcs(X , Y, len(X), len(Y)) )
'''   
