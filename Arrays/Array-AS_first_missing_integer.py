# First Missing Integer

# Problem Description
# Given an unsorted integer array A of size N. Find the first missing positive integer.
# Note: Your algorithm should run in O(n) time and use constant space.

# Problem Constraints
# 1 <= N <= 1000000
# -109 <= A[i] <= 109

# Input Format
# First argument is an integer array A.

# Output Format
# Return an integer denoting the first missing positive integer.

# Example Input

# Input 1:
# [1, 2, 0]

# Input 2:
# [3, 4, -1, 1]

# Input 3:
# [-8, -7, -6]


# Example Output

# Output 1:
# 3

# Output 2:
# 2

# Output 3:
# 1

# Example Explanation

# Explanation 1:
# A = [1, 2, 0]
# First positive integer missing from the array is 3.

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        
        num_range = len(A)+1
        
        if len(A) == 1:
            if A[0] == 1:
                return 2
            else:
                return 1
        
        # print(A)
        
        # for i in range(len(A)):
        #     if A[i] > 0 and A[i] < num_range and A[i] != A[A[i]-1]:
        #         temp = A[i]
        #         A[i] = A[temp-1]
        #         A[temp-1] = temp
        #     else:
        #         continue
        
        i = 0
        while i<len(A):
            # If you swap, do that iteration again because the number may not 
            # be in its correct place yet
            if A[i] > 0 and A[i] < num_range and A[i] != A[A[i]-1]:
                temp = A[i]
                A[i] = A[temp-1]
                A[temp-1] = temp
            else:
                i+=1
            
        # print(A)
        
        for i in range(len(A)):
            if A[i] == i+1:
                continue
            else:
                return i+1
        
        return A[-1]+1