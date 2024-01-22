import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    
    public static void helper(String s, int i, String curr){
        //note to check i with s ki length and print current at that time
         if(i == s.length()){
            System.out.println(curr+"*");
            return;

         }
         helper(s,i+1,curr+s.charAt(i));
         helper(s,i+1,curr);
         
        
    }
    public static void main(String[] args) {
      /*
      print all the possible powerset of a String
      abc => "",a,b,c,ab,ac,bc,abc i.e 2^3 =8
      
      func(string,i,cur) i=0 and curr = "" t start with
      */
      String s = "abc";
      
      //iska base case aise socho , a hai string, ans hogi  "" and "a", means liye ya nahi, and i move kara rahe 0 se 1 etc
      
      helper(s,0,"");
      
      
      
    }
}

