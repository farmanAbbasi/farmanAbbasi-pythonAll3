import java.util.*;
public class BubbleSort{

    public void bSort(int[] arr){
     int l=arr.length;
     for(int i=0;i<l-1;i++){
         for(int j=0;j<l-i-1;j++){
             if(arr[j]>arr[j+1]){
                 arr[j+1]=swap(arr[j],arr[j]=arr[j+1]);
             }
         }
     }
    }
    public int swap(int a, int b){
        return a;
    }
    public static void main(String args[]){
        int[] arr={3,20,1,0,-1,2};
        BubbleSort bs=new BubbleSort();
        bs.bSort(arr);
        System.out.println(Arrays.toString(arr));
  }
}