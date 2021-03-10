import java.io.*;
import java.util.*;

//note dfs and bfs are exactly same only this is different
public class Graph
{
    private int numVertices;
    private LinkedList<Integer> adjLists[];
 
    Graph(int vertices)
    {
        numVertices = vertices;
        adjLists = new LinkedList[vertices];
        
        for (int i = 0; i < vertices; i++)
            adjLists[i] = new LinkedList();
    }
 
    void addEdge(int src, int dest)
    {
        adjLists[src].add(dest);
    }
     boolean hasEdge(int src, int dest){
        if (adjLists[src].contains(dest)){
            return true;
        }
        return false;
    }
    public void printHelper(){
        int node=0;
        for(LinkedList<Integer> i: adjLists){
            Iterator iterator = i.iterator(); 
            System.out.print(node+" : ");
            System.out.println(i);
            //or
            // while(iterator.hasNext()){
            //     System.out.print(iterator.next() + ", ");
            // }
            // System.out.println();
            node++;
        }
    }
 
    public static void main(String args[])
    {
        Graph g = new Graph(4);
 
         g.addEdge(0, 1);
         g.addEdge(0, 2);
         g.addEdge(1, 2);
         g.addEdge(2, 3);
         g.printHelper();
    }
}