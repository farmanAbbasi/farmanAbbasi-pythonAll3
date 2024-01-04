/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.*;
public class Main
{
	public static void main(String[] args) {
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.add(5);
        pq.add(4);
        pq.add(88);
        System.out.println(pq);//4,5,88
        System.out.println(pq.peek()); //4
        
        System.out.println(pq.remove());//4 is removed
        System.out.println(pq); //5,88
        
        
        PriorityQueue<Integer> pq2 = new PriorityQueue<>(Collections.reverseOrder());
        pq2.add(5);
        pq2.add(4);
        pq2.add(88);
        System.out.println(pq2);//88,5,4
        System.out.println(pq2.peek()); //88
        
        
        System.out.println(pq2.remove());//88 is removed ,note remove only removes but poll also returns
        System.out.println(pq2); //5,4

	}
}

