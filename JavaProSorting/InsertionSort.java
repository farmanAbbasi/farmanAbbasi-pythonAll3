import java.util.*;
public class InsertionSort{

    public void iSort(int[] arr){
     int j=0;
     for(int i=1;i<arr.length;i++){
         int temp=arr[i];
         for(j=i-1;j>=0 && arr[j]>temp;j--){
             arr[j+1]=arr[j];
         }
         arr[j+1]=temp;
         //System.out.println(Arrays.toString(arr));
     }
    } 
    public static void main(String args[]){
        int[] arr={6,5,-3,-2,10,-710};
        InsertionSort is=new InsertionSort();
        is.iSort(arr);
        System.out.println(Arrays.toString(arr));
  }
}