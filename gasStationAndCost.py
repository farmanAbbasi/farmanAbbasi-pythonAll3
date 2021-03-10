#gas  = [1,2,3,4,5]
#cost = [3,4,5,1,2]
def gasMain(gas,ika):
    remaining=0
    count=0
    for i in gas:
        if i[0] + remaining >= i[1]:
            remaining+=i[0]-i[1]
            count+=1
    #print('count',count)        
    if count==len(gas):
        return ika,1
    else:
        return 0,0    




def helper(gas):
    for i in range(len(gas)):
        aa=[]
        for j in range(i,len(gas)):
            aa.append(gas[j])
        for k in range(0,i):
            aa.append(gas[k])
        #print(aa)
        ika,found=gasMain(aa,i)
        if i==len(gas)-1 and found!=1:
            return -1
        if found==1:
            return ika  
            

gas=[[1,3],[2,4],[3,5],[4,1],[5,2]]  
print(helper(gas) )

