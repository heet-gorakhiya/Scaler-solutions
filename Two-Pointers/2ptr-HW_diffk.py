# Diffk

# Given an array 'A' of sorted integers and another non negative integer k, find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.

#  Example: 
# Input : 
# A : [1 3 5] 
# k : 4

#  Output : YES as 5 - 1 = 4 
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

# Try doing this in less than linear space complexity.

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return an integer
	def diffPossible(self, A, B):
	    
	    i = 0
	    j = 1
	    
	    while i<j and j<len(A):
	        
	        diff = A[j]-A[i]
	        
	        if diff > B:
	            i+=1
	        elif diff < B:
	            j+=1
	        elif diff == B:
	            return 1
	        
	        if i == j:
	            j+=1
	    
	    return 0