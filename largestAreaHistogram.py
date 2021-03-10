a=[2,2,2,1,7]
#a=[0,1,0,2,1,0,1,3,2,1,2,1]
maxi=-9999
maximum=-9999
for i in range(0,len(a)):
    left=i
    right=i
    while(left>=0 and a[i]<=a[left]):
        left-=1
    while(right<len(a) and a[i]<=a[right]):
        right+=1    
    maxi=a[i]*(right-left-1)
    if maxi>maximum:
        maximum=maxi
print(maximum)        
       
