public class perfectSumProblem{
	public static int perfectSum(int[] arr,int k){
		return counter(arr,k,arr.length-1);
	}
	public static int counter(int[] arr,int total, int j){
		if(total==0){
			return 1;
		}
		else if(total<0){
			return 0;
		}
		else if(j<0){
			return 0;
		}
		else if(total<arr[j]){
			return counter(arr,total,j-1);
		}
		else{
			return counter(arr,total-arr[j],j-1)+counter(arr,total,j-1);
		}
	}
	
	public static void main(String ...args){
		int k=16;
	int arr[]=new int[]{2,4,6,10};
		System.out.println(perfectSum(arr,k));
	}
}