a=[0,0,0,1,1,1,1,1,1]
def one(a,l,r):
    if l>r:
        print("hero")
        return 0
    if a[r]==0:
        return 0
    elif a[l]==1:
        return r-l+1
    else:
        mid=(l+r)//2
        return one(a,l,mid)+one(a,mid+1,r)# note mid-1 and mid+1 is not given as search nahi hai
print(one(a,0,len(a)-1))    
    
