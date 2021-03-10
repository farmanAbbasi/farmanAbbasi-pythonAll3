//rectangular island
// class numberOfIslands {
//     public static int numIslands(char[][] grid) {
//         int count=0;
//         int horX=grid[0].length;
//         int verY=grid.length;
//         for(int i=0; i<verY;i++){
//             for(int j=0;j<horX;j++){
//                 if(grid[i][j]=='1'){
//                     if((i==0 || grid[i-1][j]=='0') && (j==0 || grid[i][j-1]=='0')){
//                         count++;
//                     }
//                 }
//             }
//         }
//         return count;
        
        
//     }
//     public static void main(String args[]){
//     char a[][]={{'1','1','0','0','0','0','0'},{'1','1','0','0','1','1','0'},{'0','0','0','0','1','1','0'},{'0','0','1','1','0','0','0'}};
//     System.out.println(numIslands(a));
//     }
    
// }



//any direction connected island
class Solution {
    public int numIslands(char[][] grid) {
        if(grid==null || grid.length==0){
            return 0;
        }
        int count=0;
        for(int i=0;i<grid.length;i++){
            for(int j=0;j<grid[i].length;j++){
                if(grid[i][j]=='1'){
                    count+=bfs(grid,i,j);
                }
            }
        }
        return count;
        
    }
    
    public int bfs(char[][] grid, int i, int j){
        if(i<0 ||i>=grid.length ||j<0 ||j>=grid[i].length || grid[i][j]=='0'){
            return 0;
        }
        grid[i][j]='0';
        bfs(grid,i+1,j);
        bfs(grid,i-1,j);
        bfs(grid,i,j+1);
        bfs(grid,i,j-1);
        
        // bfs(grid,i+1,j-1);
        // bfs(grid,i+1,j+1);
        // bfs(grid,i-1,j-1);
        // bfs(grid,i-1,j+1);
        
        return 1;
    }
}