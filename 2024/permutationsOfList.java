/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.
int {1,1,1}

int in={1,2,3,4}
1,2,3
1,3,2
2,1,3
2,3,1
3,1,2
3,2,1

1,1,2
{1,1,2},{2,1,1},{1,2,1}

1,1,2
1,2,1
2,1,1

*******************************************************************************/
import java.util.*;
public class Main
{
    public static List<Integer> createRemainingItemsList(List<Integer> arr, int k){
        // return a list without k for one Runtimeint 
        int c= 0;
         List<Integer> finalList = new ArrayList<>();
        for (Integer i : arr){
            if(i==k && c!=1){
                c=1;
                continue;
            }
            else{
                finalList.add(i);
            }
        }
        return finalList;
    }
    
    public static List<Integer> mergeListAndInt(int i, List<Integer> arr){
        List<Integer> finalList = new ArrayList<>();
        finalList.add(i);
        for (Integer li : arr){
            finalList.add(li);
        }
        return finalList;
    }
    
    
    public static void helper(List<Integer> arr, List<Integer> one_ans){

        if(arr.size() == 0){
            finalAns.add(one_ans);
        }
        else{
        for(int i = 0;i<arr.size();i++){
            //List<Integer> rem = createRemainingItemsList(arr,arr.get(i));
            //or
            List<Integer> rem = new ArrayList<>();
            rem.addAll(arr.subList(0,i));
            rem.addAll(arr.subList(i+1,arr.size()));
            
            List<Integer> new_ans = mergeListAndInt(arr.get(i),one_ans);
            helper(rem, new_ans);
        } 
        }
        
    }
    
   static Set<List<Integer>> finalAns = new HashSet<>();

	public static void main(String[] args) {
	    List<Integer> input = new ArrayList<>(Arrays.asList(1,2,1));
	    List<Integer> one_ans = new ArrayList<>();
	    helper(input, one_ans);
	    System.out.println(finalAns);	    
	    System.out.println(finalAns.size());
	   // for (1 1 2)->[[2, 1, 1], [1, 1, 2], [1, 2, 1]]
    //     3
//     for (1,2,3)-> [[3, 2, 1], [1, 2, 3], [3, 1, 2], [2, 1, 3], [2, 3, 1], [1, 3, 2]]
// 6

	    
	}
}











