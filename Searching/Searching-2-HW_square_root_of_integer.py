# Square Root of Integer

# Problem Description
# Given an integer A.
# Compute and return the square root of A.
# If A is not a perfect square, return floor(sqrt(A)).
# DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.
# NOTE: Do not use sort function from standard library. Users are expected to solve this in O(log(A)) time.

# Problem Constraints
# 0 <= A <= 1010

# Input Format
# The first and only argument given is the integer A.

# Output Format
# Return floor(sqrt(A))

# Example Input

# Input 1:
#  11

# Input 2:
#  9

# Example Output

# Output 1:
#  3

# Output 2:
#  3

# Example Explanation

# Explanation:
#  When A = 11 , square root of A = 3.316. It is not a perfect square so we return the floor which is 3.
#  When A = 9 which is a perfect square of 3, so we return 3.

class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        
        if A == 0:
            return 0
        
        low = 1
        high = A
        
        while low <= high:
            
            mid = low + (high-low)//2
            
            if mid*mid <= A and (mid+1)*(mid+1) > A:
                return mid
            elif mid*mid < A:
                low = mid+1
            else:
                high = mid-1
                
        return low