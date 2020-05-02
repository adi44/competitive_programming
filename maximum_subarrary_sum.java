import java.io.*;
import java.util.*;
/*Algorithm 
Here we need to find the maximum sum of the subarray. in order to find the maximum sum of the sub array
we will use the kandere's algorithm. According to this algorithm, we will take sum as the initial element of the array.
once we will take the initial element of array. we will sum with its next element. if the sum would be more than the current element we will continue taking sum
else we will put the value of current sum as the current element. 
here we are doing this because we need to calculate the sum of next subarray if current elment is greater than the sum after adding it to the sum. 
which means if the sum is getting less after adding current element, then we need to calculate sum of new subarray.*/


class maximum_subarray_sum{
static int maximum_subarray_sum(int arr[])
{
	int maximum_sum=arr[0];
	int current_sum=maximum_sum;
	for(int i=0;i<arr.length;i++)
	{
		current_sum=Math.max(arr[i]+current_sum,arr[i]);
		maximum_sum=Math.max(current_sum,maximum_sum);
	}
	return maximum_sum;
}
public static void main(String args[])
{
	int arr[]={-1,-4,3,7,5,-2};
	System.out.println(maximum_subarray_sum(arr));
}
}
