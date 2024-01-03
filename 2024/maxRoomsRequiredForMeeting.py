#max number of meeting rooms required for all meeting
#in greedy algorightms by freecode amp
a= [[0,30],[5,10],[15,20]]
arr = []

for s,e in a:
    arr.append((s,1))
    arr.append((e,-1))
arr.sort(key = lambda x: x[0])
print(arr)#[(0, 1), (5, 1), (10, -1), (15, 1), (20, -1), (30, -1)]

ans=0 
curr=0
for _,i in arr:
    curr = curr+i 
    ans =max(curr,ans)
print(ans)    
    
