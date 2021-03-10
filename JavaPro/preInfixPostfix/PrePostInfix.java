import java.util.*;

class PrePostInfix{

    public static boolean isOperator(char c){
        if(c=='+' || c=='-' || c=='*' || c=='/'){
            return true;
        }
        return false;
    }
    public static String prefixToPostfix(String query){
        Stack<String> s=new Stack<>();
        int i=query.length()-1;
        while(i>=0){
            if(!isOperator(query.charAt(i))){
                s.push(query.charAt(i)+"");
            }else{
                String temp1=s.pop();
                String temp2=s.pop();
                s.push(temp1+temp2+query.charAt(i));
            }
            i--;
        }
        return s.pop();
    }
    public static String postfixToPrefix(String query){
        Stack<String> s=new Stack<>();
        int i=0;
        while(i<query.length()){
            if(!isOperator(query.charAt(i))){
                s.push(query.charAt(i)+"");
            }
            else{
                String temp1=s.pop();
                String temp2=s.pop();
                s.push(query.charAt(i)+temp2+temp1);
            }

            i++;
        }
      return s.pop();
    }
    public static String prefixToInfix(String query){
            Stack<String> s=new Stack<>();
            int i=query.length()-1;
            while(i>=0){
                if(!isOperator(query.charAt(i))){
                 s.push(query.charAt(i)+"");
                }else{
                    String temp1=s.pop();
                    String temp2=s.pop();
                    s.push("("+temp1+query.charAt(i)+temp2+")");
                }
                i--;
            }
            return s.pop();
    }

    public static void main(String args[]){
        String query="*-A/BC-/AKL";

        String result=prefixToPostfix(query);
        System.out.println("Postfix :"+ result);

        result=postfixToPrefix(result);
        System.out.println("Prefix :"+ result);

        result=prefixToInfix(result);
        System.out.println("Infix :"+ result);


    }
}

