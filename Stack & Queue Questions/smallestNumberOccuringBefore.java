import java.util.*;

public class Main{
    
     public static void prevSmaller(int[] A) {
        Stack<Integer> s= new Stack<>();
        s.push(99999);
        int []ans=new int[A.length];
        for(int i=0;i<A.length;i++){
            ans[i]=-1;
        }
        boolean valueFound=false;
        for(int i=0;i<A.length;i++){                       // A = [4, 5, 2, 10, 8]
            valueFound=false;                                       //  G = [-1, 4, -1, 2, 2]
            while(!s.isEmpty() && !valueFound){
                if(A[i]>s.peek()){
                    ans[i]=s.peek();
                    valueFound=true;
                }
                else{
                    s.pop();
                }
            }
            s.push(A[i]);
        }
        System.out.println(Arrays.toString(ans));
 }
    public static void main(String args[]){
         prevSmaller(new int[]{4,5,2,10,8});
    }
}