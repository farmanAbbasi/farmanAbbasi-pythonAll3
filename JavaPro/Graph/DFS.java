import java.util.*;
import java.io.*;
class Graph{
    
    private int vertices;
    private int[][] adjMatrix;
    
    Graph(int vertices){
        this.vertices=vertices;
        adjMatrix=new int[vertices][vertices];
        for(int i=0;i<this.vertices;i++){
            for(int j=0;j<this.vertices;j++){
                adjMatrix[i][j]=0;
            }
        }
    }
    
    public void addEdge(int x, int y){
        adjMatrix[x][y]=1;
        adjMatrix[y][x]=1;
    }
    public void deleteEdge(int x, int y){
        adjMatrix[x][y]=0;
        adjMatrix[y][x]=0;
    }
    public boolean hasEdge(int x, int y){
        if(adjMatrix[x][y]==1){
            return true;
        }
        return false;
        
    }
    public void printHelper(){

     for(int i=0;i<vertices;i++){
            for(int j=0;j<vertices;j++){
                System.out.print(adjMatrix[i][j]);
            }
            System.out.println();
        }  
     System.out.println();    
    }
    
    public void dfs(int startNode){
        boolean visited[]=new boolean[vertices];
        for(int i=0;i<vertices;i++)
        {
            visited[i]=false;
        }
        
        helperDfs(startNode,visited);
        
    }
    
    public void helperDfs(int startNode, boolean visited[]){
        //     visited[startNode]=true;
        //     System.out.println(startNode);
        // for(int i=0;i<visited.length;i++){
        //     if(hasEdge(startNode,i) && visited[i]==false){
        //         helperDfs(i,visited);
        //     }
        // }
        //or 
        Stack<Integer> s=new Stack<>();
        visited[startNode]=true;
        System.out.println("By stack"+startNode);
        s.push(startNode);
        while(!s.isEmpty()){
            int v=getAdjacentUnvisitedVertex(s.peek(),visited);
            if(v==-1){
                s.pop();
            }
            else{
                visited[v]=true;
                System.out.println(v);
                s.push(v);
            }
    }

    }  

    public void bfs(int startNode){
      boolean visited[] =new boolean[vertices];
       for(int i=0;i<vertices;i++){
           visited[i]=false;
       }
       helperBfs(startNode,visited);
    } 

    public void helperBfs(int startNode,boolean []visited){
        Queue<Integer> q=new LinkedList<>();
        
        visited[startNode]=true;
        System.out.println(startNode+"by BFS");
        q.add(startNode);

        while(!q.isEmpty()){
            int x=q.remove();
            int v;
            while((v=getAdjacentUnvisitedVertex(x,visited))!=-1){
                visited[v]=true;
                System.out.println(v);
                q.add(v);
            }
            
        }
        

    }

    public  int getAdjacentUnvisitedVertex(int v,boolean[] visited){
        for(int i=0;i<vertices;i++){
            if(hasEdge(v,i) && visited[i]==false){
                return i;
            }
        }
        return -1;
    }
}

public class DFS

{   
	public static void main(String[] args) {
        // Note only for connected graphs
		Graph g=new Graph(7);
	    g.addEdge(0, 1);
        g.addEdge(0, 3);
        g.addEdge(1, 0);
        g.addEdge(2,1);
        g.addEdge(2,4);
        g.addEdge(3,0);
        g.addEdge(3, 1);
        g.addEdge(3,2);
        g.addEdge(3, 4);
        g.addEdge(4,2);
        g.addEdge(4,3);
        g.addEdge(5,6);
        g.addEdge(4,5);//if we remove this it becomes unconnected graph 

        
        
    	g.printHelper();
		g.dfs(0);
        g.bfs(0);		
	}
}
