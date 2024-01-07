'''
input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]
          
         1: punctuation =".","!","?" ->  here
         2: order of occurence  -to work
'''
def compare(a): #["practice", [3,10] ] , ["xyz", [3,8] ] python2
                      # -1 (a)                     1(b)
  if a[1][0] <b[1][0]:
    return 1
  elif a[1][0] >b[1][0]:
    return -1
  else:
    #both matches
    if a[1][1] < b[1][1]:
      return -1
    else:
      return 1
def compare2(a): # all same only a and b is only a
    if a[1][0] < a[1][0]:
        return 1
    elif a[1][0] > a[1][0]:
        return -1
    else:
        # both matches
        if a[1][1] < a[1][1]:
            return -1
        else:
            return 1  
def compare_(a,b):  # [5,2]   [3,4].  python2
  if a[0] < b[0]:
     return -1
  else:
    return 1
def compare_2(a):  # [5,2]   [3,4].  python3
  return a[0]  
  
# or  
def compare_2b(a):  # [5,2]   [3,4].  python3, not all same as 2 only a and b is now a
  if a[0] < a[0]:
     return -1
  else:
    return 1 
  
  
def remove_Punctuation(string):
  ans = ""
  for c in string:
    if (c >="a" and c<="z") or (c >= "0" and c<="9"):
      ans+=c
  return ans    
      
  
  
def word_count_engine(document):
  final_list = []
  dicty = {}
  document_array = document.split()
  
  for item in range(len(document_array)):
    clear_word = remove_Punctuation(document_array[item].lower())
    
    if clear_word in dicty:
      
      temp = dicty[clear_word] #[1,0] -> [2,0]
      temp[0] = temp[0]+1
      dicty[clear_word] = temp #[2,0] [count,occurence]
    else:
      dicty[clear_word] = [1,item]
  #dicty will have all the values not in order
  for i in dicty:
    temp = []
    temp.extend([i,dicty[i]])
    final_list.append(temp)
      
  final_list.sort(key = compare2)
  
  return [ [i[0],str(i[1][0])]  for i in final_list]

print(word_count_engine("Practice makes perfect. you'll only get Perfect by practice. just practice!"))

  
