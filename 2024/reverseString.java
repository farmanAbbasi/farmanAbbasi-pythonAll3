/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.*;
public class Main
{
	public static void main(String[] args) {

		char[] arr =  {'p', 'e', 'r', 'f', 'e', 'c', 't', ' ',
                'm', 'a', 'k', 'e', 's', ' ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'd','a','i','l','y'};
        char[] ans = new char[arr.length];        
        Stack<Character> stack = new Stack<>();
        int i = ans.length-1;
        for(char c : arr){
            
            while(!stack.isEmpty() && c == ' '){
                   ans[i] = stack.pop();
                   i-=1; 
            }
            stack.push(c);
            
            if(c == ' '){
                ans[i] = stack.pop();
                i-=1;  
            }
             
        }
        
        while(!stack.isEmpty()){
            ans[i] = stack.pop();
                i-=1;  
        }
        for (char c: ans){
            System.out.print(c); //daily practice makes perfect
        }
        
       
	}
}
// in this i am using a new arr and a stack but this can be done by without using a stack and reversing the string and then reversing once we get a space again


arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', ' ',
                'm', 'a', 'k', 'e', 's', ' ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

def reverse(arr,s,e):
    while s<e:
        arr[s], arr[e] = arr[e], arr[s]
        s+=1 
        e-=1
    return arr    

arr = reverse(arr,0,len(arr)-1)  
print(arr)

c = 0
for i in range(len(arr)):
    if arr[i] == " ":
        arr = reverse(arr,c,i-1)
        c=i+1
    if i == len(arr)-1:
        arr = reverse(arr,c,i)

print(arr) 

# time: O(N)¯¸
# space: O
#['p', 'r', 'a', 'c', 't', 'i', 'c', 'e', ' ', 'm', 'a', 'k', 'e', 's', ' ', 'p', 'e', 'r', 'f', 'e', 'c', 't']¯¸
        
        
    
