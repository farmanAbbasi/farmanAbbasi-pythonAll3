




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
        if matrix[rnew][cnew]==-1 or matrix[rnew][cnew]==2:
            continue
        return [rnew,cnew]
    return -1    


def findPathInMaze(matrix,sourceA,targetA):
    stackMe=[]
    stackMe.append(sourceA)
    matrix[sourceA[0]][sourceA[1]]=2
    
    while len(stackMe)>0:
        v=getPathsWhereCanGo(matrix,stackMe[-1])
        
        if v==-1:
            stackMe.pop()
        else:
            stackMe.append(v)
            matrix[v[0]][v[1]]=2
            
            if v==targetA:
                break
    return stackMe        
            
    

matrix=[[0,-1,-1,-1],[0,0,-1,0],[0,0,-1,-1],[-1,0,0,0]]
sourceA=[0,0]
targetA=[3,3]
print(findPathInMaze(matrix,sourceA,targetA))




