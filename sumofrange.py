#!/usr/bin/env python3
'''In this question we need to find the sum of the subarray given in the question. for solving this question, we are using the dynamic programming
since it will reduce the time complexity. and it would be done in O(1) time.

Algorithm to solve this question.
Step 1: initialise a empty list with an initial element equal to initial element of the array.
step 2: run a loop from 1->n and fill it with the sum uptil the current element.
Step 3: in order to get sum of given range just subtract the value of index(initial value-1) and value of index(final value)
step 4: return the sum
'''
array = [-1,-2,4,3,2,9,8]
sum_array=[]
sum_array.append(array[0])
for i in range(1,len(array)-1):
	sum_array.append(sum_array[i-1]+array[i])

print(sum_array[5]-sum_array[0])


