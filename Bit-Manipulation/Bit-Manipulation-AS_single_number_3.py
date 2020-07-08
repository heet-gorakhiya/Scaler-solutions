# Single Number III

# Problem Description
# Given an array of numbers A , in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
# Note: Output array must be sorted.

# Problem Constraints
# 2 <= |A| <= 100000
# 1 <= A[i] <= 109

# Input Format
# First argument is an array of interger of size N.

# Output Format
# Return an array of two integers that appear only once.

# Example Input

# Input 1:
# A = [1, 2, 3, 1, 2, 4]

# Input 2:
# A = [1, 2]

# Example Output

# Output 1:
# [3, 4]

# Output 2:
# [1, 2]

# Example Explanation

# Explanation 1:
#  3 and 4 appear only once.

# Explanation 2:
#  1 and 2 appear only once.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        
        cumulative_xor = A[0]
        pos = 0
            
        for i in range(1,len(A)):
            cumulative_xor = cumulative_xor^A[i]
            
        for i in range(32):
            if (cumulative_xor&(1<<i)) != 0:
                pos = i
                break
            
        num_1 = 0
        num_2 = 0
        
        for i in range(len(A)):
            if (A[i]&(1<<pos)) != 0:
                num_1 = num_1^A[i]
            else:
                num_2 = num_2^A[i]
                
        if num_1>=num_2:
            return [num_2,num_1]
        else:
            return [num_1,num_2]