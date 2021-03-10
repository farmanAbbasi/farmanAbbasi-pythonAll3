def findWater(arr, n): 
	left = [0]*n 
	right = [0]*n 
	water = 0
	left[0] = arr[0] 
	for i in range( 1, n): 
		left[i] = max(left[i-1], arr[i])
	print(left)
        
	right[n-1] = arr[n-1] 
	for i in range(n-2, -1, -1): 
		right[i] = max(right[i+1], arr[i])
	print(right)
	for i in range(0, n): 
		water += min(left[i],right[i]) - arr[i] 

	return water 

arr = [5,10,5,15] 
n = len(arr) 
print("Maximum water that can be accumulated is",findWater(arr, n)) 

