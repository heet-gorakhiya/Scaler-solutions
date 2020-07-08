# Max Distance

# Problem Description
# Given an array A of integers of size N. Find the maximum of value of j - i such that A[i] &lt;= A[j].

# Problem Constraints
# 1 <= N <= 1000000
# -109 <= A[i] <= 109

# Input Format
# First argument is an integer array A of size N.

# Output Format
# Return an integer denoting the maximum value of j - i.

# Example Input

# Input 1:
# A = [3, 5, 4, 2]


# Example Output

# Output 1:
# 2

# Example Explanation

# Explanation 1:
# For A[0] = 3 and A[2] = 4, the ans is (2 - 0) = 2. 

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        
        # max_dist = 0
        # i = 0
        # j = 0
        # size = len(A)
        # left_min = [0]*size
        # right_max = [0]*size
        
        # left_min[0] = A[0]
        # for i in range(1,size):
        #     left_min[i] = min(A[i], left_min[i-1])
        
        # right_max[size-1] = A[size-1] 
        # for j in range(size-2, -1, -1): 
        #     right_max[j] = max(A[j], right_max[j+1])
            
        # max_dist = -1
        # while j<size and i<size: 
        #     if left_min[i] < right_max[j]: 
        #         max_dist = max(max_dist, j-i) 
        #         j+=1
        #     else: 
        #         i+=1
        
        # return max_dist
        
        n = len(A)
        
        if n == 1:
            return 0
        
        maxDiff = 0; 
    	LMin = [0] * n 
    	RMax = [0] * n 
    	
    	LMin[0] = A[0] 
    	for i in range(1, n): 
    		LMin[i] = min(A[i], LMin[i - 1]) 

    	RMax[n - 1] = A[n - 1] 
    	for j in range(n - 2, -1, -1): 
    		RMax[j] = max(A[j], RMax[j + 1]); 

    	i, j = 0, 0
    	maxDiff = -1
    	while (j < n and i < n): 
    		if (LMin[i] <= RMax[j]): 
    			maxDiff = max(maxDiff, j - i) 
    			j = j + 1
    		else: 
    			i = i+1
    
    	return maxDiff