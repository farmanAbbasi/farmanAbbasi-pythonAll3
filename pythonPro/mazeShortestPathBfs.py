def getPathsWhereCanGo(matrix,source):
    r=source[0]
    c=source[1]
    rr=[-1,1,0,0]
    rc=[0,0,1,-1]
    for i in range(4):
        rnew=r+rr[i]
        cnew=c+rc[i]
    
        if rnew<0 or cnew<0 or rnew>=len(matrix) or cnew>=len(matrix[0]):
            continue
        if matrix[rnew][cnew]==1 or matrix[rnew][cnew]==2:
            continue
        return [rnew,cnew]
    return -1 



def findPathInMazeBfs(matrix,sourceA,targetA):
    queueMe=[]
    queueMe.append(sourceA)
    matrix[sourceA[0]][sourceA[1]]=2
    #print(sourceA)
    pathObject={}
    while len(queueMe)>0:
        cell=queueMe.pop(0)
        
        while(getPathsWhereCanGo(matrix,cell) != -1):
            v=getPathsWhereCanGo(matrix,cell)
            queueMe.append(v)
            #print("parent",cell)
            #print(v)
            matrix[v[0]][v[1]]=2
            #note child : parent
            pathObject[str(v)]=cell
            if(v==targetA):
                return pathObject
            
            
    return -1

#https://stackoverflow.com/questions/8922060/how-to-trace-the-path-in-a-breadth-first-search

def findPath(pathObject,sourceA,targetA):
    ansArray=[]
    ansArray.append(targetA)
    while ansArray[-1] != sourceA:
        ansArray.append(pathObject[str(ansArray[-1])])
    ansArray.reverse()      
    return ansArray
    
    
            
matrix=[
[0,0,1,1,0],
[0,0,0,1,0],
[1,1,0,0,0]
]



sourceA=[0,0]
targetA=[len(matrix)-1,len(matrix[0])-1]
#print(findPathInMazeDfs(matrix,sourceA,targetA))
pathObject=findPathInMazeBfs(matrix,sourceA,targetA)

print(pathObject)
if pathObject!=-1:
    result=findPath(pathObject,sourceA,targetA)
    print(result)





