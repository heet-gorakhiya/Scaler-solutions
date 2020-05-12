# Delete one
# Problem Description
# Given an integer array A of size N. You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.

# Find the maximum value of GCD.

# Problem Constraints
# 2 <= N <= 105
# 1 <= A[i] <= 109

# Input Format
# First argument is an integer array A.

# Output Format
# Return an integer denoting the maximum value of GCD.

# Example Input
# Input 1:
#  A = [12, 15, 18]
# Input 2:
#  A = [5, 15, 30]

# Example Output
# Output 1:
#  6
# Output 2:
#  15

# Example Explanation
# Explanation 1:
#  If you delete 12, gcd will be 3.
#  If you delete 15, gcd will be 6.
#  If you delete 18, gcd will 3.
#  Maximum value of gcd is 6.

# Explanation 2:
#  If you delete 5, gcd will be 15.
#  If you delete 15, gcd will be 5.
#  If you delete 30, gcd will be 5.


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        def gcd(x, y):
            if y==0:
                return abs(x)
            else:
                return gcd(y, x%y)
        
        if len(A)==1:
            return 0
        if len(A)==2:
            return max(A)
        
        rev_A = list(reversed(A))
        prec_left = []
        prec_right = []
        prec_left.append(A[0])
        new_gcd_left = A[0]
        prec_right.append(rev_A[0])
        new_gcd_right = rev_A[0]
        max_gcd = 0
        
        for i in range(1,len(A)):
            new_gcd_left = gcd(new_gcd_left,A[i])
            new_gcd_right = gcd(new_gcd_right,rev_A[i])
            prec_left.append(new_gcd_left)
            prec_right.append(new_gcd_right)
            
        prec_right = list(reversed(prec_right))
        
        for i in range(len(A)):
            if i==0:
                left = 1
                right = prec_right[i+1]
            elif i==(len(A)-1):
                left = prec_left[i-1]
                right = 1
            else:
                left = prec_left[i-1]
                right = prec_right[i+1]
            
            curr_gcd = gcd(left, right)
            
            if curr_gcd > max_gcd:
                max_gcd = curr_gcd
            
        return max_gcd