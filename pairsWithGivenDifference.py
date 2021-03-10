def find_pairs_with_given_difference(arr, k):
  dicty={}
  result=[]
  for a in arr:
      dicty[a]=1
  for a in arr:
      #print(dicty.get(a-k))
      if dicty.get(a-k):
          result.append([a,a-k])
  print(dicty) 
  print(sorted(result, key =lambda x: x[0]))
  
#find_pairs_with_given_difference([1,5,3,4,5],2)

#got on pramp with the indian guy
#learned three things
# can add all the elemnts in dict before hand
# can add before check
#or can add after check
def get_indices_of_item_wights(arr, limit):
  dicty={}
  result=[]
    
  for i in range(len(arr)):
    result=[]
    if dicty.get(limit-arr[i])!=None:
      if dicty.get(limit-arr[i])>i:
        result.append(dicty.get(limit-arr[i]))
        result.append(i)
      else:
        result.append(i)
        result.append(dicty.get(limit-arr[i]))
      return result
    else:
      dicty[arr[i]]=i
  print(dicty)    
  return result 
    
    
print(get_indices_of_item_wights([4, 16, 10, 15, 6,7],22)) 
