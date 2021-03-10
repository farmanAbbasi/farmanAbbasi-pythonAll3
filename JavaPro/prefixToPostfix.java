import java.util.*;
public class prefixToPostfix{
	public static boolean isOperator(char letter){
		
		switch(letter){
			case '+':
			case '-':
			case '*':
			case '/':
		    return true;
		}
		return false;
	}
	
	public static String postFixer(String prefix){
		int x=prefix.length();
		Stack<String> s=new Stack();
		for(int i=x-1;i>=0;i--){
			if(isOperator(prefix.charAt(i))){
				String temp="";
	            String temp2="";
				temp=s.pop();
				temp2=temp;
				temp=s.pop();
				temp2=temp2+temp+prefix.charAt(i);
				s.push(temp2);
				
			}
			else{
				s.push(prefix.charAt(i)+"");
			}
		}
		return s.peek();
	}
	
	public static void main(String ...args){
		String prefix= "*-A/BC-/AKL";
		System.out.println("Prefix :"+prefix);
		System.out.println("Postfix :"+postFixer(prefix));
	}
}