import java.util.*;
class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums==null || nums.length==0 || k==0){
            return new int[]{};
        }
        PriorityQueue<Integer> pq=new PriorityQueue<>(k,Collections.reverseOrder());
        int arr[]=new int[nums.length-k+1];
        int j=0;
        int i=0;
        //sare numbers traverse honge
        //for k=3 , max heap ka first wla pick hoga save hoga aur delete 0th index wala hoga and so on
        while(i<nums.length){
           while(pq.size()<k){
               pq.add(nums[i]);
               i++;
           }
            arr[j]=pq.peek();
            pq.remove(nums[j]);
            j++;   
        }
       // System.out.print(Arrays.toString(arr));
        return arr;   
    }
    
}