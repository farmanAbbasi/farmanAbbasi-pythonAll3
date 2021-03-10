//see quicksort from mycodeschool.com
import java.util.*;
public class QuickSort{

    public void QSort(int[] arr,int start, int end){
        if (start>=end) return;
        int partition=partitioning(arr,start,end);
        QSort(arr,start,partition-1);
        QSort(arr,partition+1,end);
    }

    public int partitioning(int[] arr,int start,int end){
        //note: its uses some of the logic from two pointr mthod
        int m=start;
        int pivot=arr[end];
        for(int i=start;i<end;i++){
            if(arr[i]<=pivot){
                int temp=arr[i];
                arr[i]=arr[m];
                arr[m]=temp;
                m+=1;
            }
        }
        int temp=arr[end];
        arr[end]=arr[m];
        arr[m]=temp;
        return m;
    } 

    public static void main(String args[]){
        int[] arr={3,20,1,0,-1,2};
        QuickSort qs=new QuickSort();
        qs.QSort(arr,0,arr.length-1);
        //System.out.println(qs.partitioning(arr,0,arr.length-1));
        System.out.println(Arrays.toString(arr));
    }
}