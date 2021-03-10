
public class Pascal
{   
    public static int[][] pascal(int n){
        int[][] grid=new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<=i;j++){
                // if(j==0||i==j){
                //     grid[i][j]=1;
                // }
                // else{
                //     grid[i][j]=grid[i-1][j-1]+grid[i-1][j];
                // }
                //or 
                grid[i][j]=pascalRecursive(i,j);
            }
        }
        return grid;
    };
    
    public static int pascalRecursive(int i,int j){
        if(j==0 || i==j){
            return 1;
        }
        else{
            return pascalRecursive(i-1,j-1)+pascalRecursive(i-1,j);
        }
        
    }
    
    public static void printHelper(int [][]result){
        int n=result.length;
		for(int i=0;i<n;i++){
		    for(int j=0;j<=i;j++){
		        System.out.print(result[i][j]+" ");
		    }
		    System.out.println();
		}
    }
    
    public static void printInDesign(int result[][]){
        int n=result.length;
        //k is for the space between stars
        int k=1;
        //l is for picking j element
        int l=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<2*n;j++){
                if(j>=n-i && j<=n+i){
                    if(k==1){
                        k=k*-1;
                    System.out.print(result[i][l]);
                    //System.out.print('*');
                    l++;
                    }
                    else{
                        k=k*-1;
                        System.out.print(' ');
                    }
                }
                else{
                    System.out.print(' ');
                }
            }
            l=0;
            k=1;
            System.out.println();
        }
    }
	public static void main(String[] args) {
	    int n=10;
	    //getting a n*n matrix of reult without any space;
		int[][] result=pascal(n);
		//printHelper(result);
		printInDesign(result);
		
	}
}
