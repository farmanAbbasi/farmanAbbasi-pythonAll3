def lps(str): 
    n = len(str) 
  
    # Create a table to store results of subproblems 
    L = [[0 for x in range(n)] for x in range(n)] 
  
    # Strings of length 1 are palindrome of length 1 
    for i in range(n): 
        L[i][i] = 1
    # cl is length of substring 
    for cl in range(2, n+1):
        #if n is 5 and cl =2 toh 5-2+1=4, [(0,1 wla),(1,2 wala),(2, 3 wala),(3,4 wla)]
        for i in range(n-cl+1):
            '''i is start of substring and j is the last of that substring as hume
            first and last hi toh compare karna hai'''
            j = i+cl-1
            if str[i] == str[j] and cl == 2: 
                L[i][j] = 2
            elif str[i] == str[j]: 
                L[i][j] = L[i+1][j-1] + 2
            else: 
                L[i][j] = max(L[i][j-1], L[i+1][j]); 
  
    return L[0][n-1]
  
# Driver program to test above functions 
seq = "GEEKS FOR GEEKS"
n = len(seq) 
print("The length of the LPS is " + str(lps(seq)))


'''
remember if 5 elements in array taken 2 at a time, then what size array is formed
5-2+1=4
remember if 5 elements in array taken 3 at a time, then what size array is formed
5-3+1=3
remember if 5 elements in array taken 5 at a time, then what size array is formed
5-5+1=1
i.e n-cl+1


'''

'''
 Python 3 program of above approach 
  
# A utility function to get max  
# of two egers  
def max(x, y): 
    if(x > y): 
        return x 
    return y 
      
# Returns the length of the longest  
# palindromic subsequence in seq  
def lps(seq, i, j): 
      
    # Base Case 1: If there is  
    # only 1 character  
    if (i == j): 
        return 1
  
    # Base Case 2: If there are only 2  
    # characters and both are same  
    if (seq[i] == seq[j] and i + 1 == j): 
        return 2
      
    # If the first and last characters match  
    if (seq[i] == seq[j]): 
        return lps(seq, i + 1, j - 1) + 2
  
    # If the first and last characters 
    # do not match  
    return max(lps(seq, i, j - 1),  
               lps(seq, i + 1, j)) 
  
# Driver Code 
if __name__ == '__main__': 
    seq = "GEEKSFORGEEKS"
    n = len(seq) 
    print("The length of the LPS is",  
                  lps(seq, 0, n - 1)) 
      

'''

  
