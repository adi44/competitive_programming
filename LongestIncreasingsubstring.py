#!/usr/bin/env python3
''' In this question , we are going to find the longest common substring, among two given substrings. in order to solve this question
we will be making use of dynamic programming. so we will create a matrix with all 0s in the initial row and column

Step 1: we need to initialise a matrix with size len(String)+1, len(string)+1.
Step 2: once you initialise matrix you can start comparing the letter of each string'''

def LongestCommonSubstring(X,Y,m,n):
	LCSmatrix=[[0 for k in range(n+1)] for l in range(m+1)]
	result=0
	for i in range(m+1):
		for j in range(n+1):
			if(i==0 or j==0):
				LCSmatrix[i][j]=0
			elif (X[i-1]==Y[j-1]) :
				LCSmatrix[i][j]=LCSmatrix[i-1][j-1]+1
				result= max(result, LCSmatrix[i][j])
			else:
				LCSmatrix[i][j]=0
	return result

	

X = 'HELLO'
Y = 'HELLOS'
  
m = len(X) 
n = len(Y) 
  
print('Length of Longest Common Substring is', LongestCommonSubstring(X, Y, m, n)) 
