INF=999999
V=4
# A utility function to print the solution 
def printGraph(dist): 
    
    for i in range(V): 
        for j in range(V): 
            if(dist[i][j] == INF): 
                print("oo ",end=' ') 
            else: 
                print("{}".format(dist[i][j]).ljust(3,' '),end=' ') 
            if j == V-1: 
                print(" ")

def applyFloydWarshalls(G):
    for k in range(V):
        for i in range(V):
            for j in range(V):
                G[i][j]=min(G[i][j],(G[i][k]+G[k][j]))
    return G
            
G = [[0,5,INF,10], 
     [INF,0,3,INF], 
     [INF, INF, 0,1], 
     [INF, INF, INF,0] ]
print('Initial graph')
printGraph(G)#initial graph

G=applyFloydWarshalls(G)
print ("Following matrix shows the shortest distances between every pair of vertices") 
printGraph(G)


