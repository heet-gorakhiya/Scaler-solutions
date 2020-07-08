# Maximum Absolute Difference

# Problem Description
# You are given an array of N integers, A1, A2, .... AN.
# Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.

# Problem Constraints
# 1 <= N <= 100000
# -10^9 <= A[i] <= 10^9

# Input Format
# First argument is an integer array A of size N.

# Output Format
# Return an integer denoting the maximum value of f(i, j).

# Example Input

# Input 1:
# A = [1, 3, -1]

# Input 2:
# A = [2]


# Example Output

# Output 1:
# 5

# Output 2:
# 0


# Example Explanation

# Explanation 1:
# f(1, 1) = f(2, 2) = f(3, 3) = 0
# f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
# f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
# f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5

# So, we return 5.

# Explanation 2:
# Only possibility is i = 1 and j = 1. That gives answer = 0.

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        
        # result = -10**15
        # size = len(A)
        
        # for i in range(0, size):
        #     for j in range(i, size):
        #         if result > (abs(A[i]-A[j]) + abs(i-j)):
        #             result = (abs(A[i]-A[j]) + abs(i-j))
        
        max_1 = -10**15
        min_1 = 10**15
        max_2 = -10**15
        min_2 = 10**15
        
        for i in range(len(A)):
            max_1 = max(A[i]+i, max_1)
            min_1 = min(A[i]+i, min_1)
            max_2 = max(A[i]-i, max_2)
            min_2 = min(A[i]-i, min_2)
            
        result = max(max_1-min_1, max_2-min_2)
                    
        return result