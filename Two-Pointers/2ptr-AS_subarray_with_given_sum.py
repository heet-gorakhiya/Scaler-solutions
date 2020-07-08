# Sub-array with given sum

# Problem Description
# Given an array of positive integers A and an integer B, find and return first continuous subarray which adds to B.
# If the answer does not exist return an array with a single element "-1".
# First sub-array means the sub-array for which starting index in minimum.

# Problem Constraints
# 1 <= length of the array <= 100000
# 1 <= A[i] <= 10^9
# 1 <= B <= 10^9

# Input Format
# The first argument given is the integer array A.
# The second argument given is integer B.

# Output Format
# Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single element "-1".

# Example Input

# Input 1:
#  A = [1, 2, 3, 4, 5]
#  B = 5

# Input 2:
#  A = [5, 10, 20, 100, 105]
#  B = 110


# Example Output

# Output 1:
#  [2, 3]

# Output 2:
#  -1

# Example Explanation

# Explanation 1:
#  [2, 3] sums up to 5.

# Explanation 2:
#  No subarray sums up to required number.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        
        if len(A) == 0:
            return [-1]
        if len(A) == 1:
            if A[0] == B:
                return [A[0]]
            return [-1]
        if len(A) == 2:
            if B in A:
                return [B]
        
        i=0
        j=0
        curr_sum = 0
        
        while j<len(A):
            
            if curr_sum == B:
                return A[i:j]
            
            if curr_sum < B:
                curr_sum += A[j]
                j += 1
            elif curr_sum > B:
                curr_sum -= A[i]
                i += 1
        
        # All the commented code gives TLE
        
        # i=0
        # j=1
        # curr_sum = A[0] + A[1]    
            
        # while i <= j and j<len(A): 
        
            # if curr_sum < B or i==j:
            #     if j<len(A)-1:
            #         j += 1
            #         curr_sum += A[j]
            #     else:
            #         break
                
            # elif curr_sum > B:
            #     if i<len(A)-1:
            #         curr_sum -= A[i]
            #         i += 1
            #     else:
            #         break
            
            # if curr_sum == B:
            #     return A[i:j+1]
                
        return [-1]