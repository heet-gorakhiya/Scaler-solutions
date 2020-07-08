# Divide Integers

# Problem Description
# Divide two integers without using multiplication, division and mod operator.
# Return the floor of the result of the division.
# Also, consider if there can be overflow cases i.e output is greater than INT_MAX, return INT_MAX.
# NOTE: INT_MAX = 2^31 - 1

# Problem Constraints
# -231 <= A, B <= 231-1
# B!= 0

# Input Format
# First argument is an integer A denoting the dividend.
# Second argument is an integer B denoting the divisor.

# Output Format
# Return an integer denoting the floor value of the division.

# Example Input

# Input 1:
#  A = 5
#  B = 2

# Input 2:
#  A = 7
#  B = 1

# Example Output

# Output 1:
#  2

# Output 2:
#  7

# Example Explanation

# Explanation 1:
#  floor(5/2) = 2

class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def divide(self, A, B):
	    
	    sign = (-1 if((A<0)^(B<0)) else 1)
	    A = abs(A)
	    B = abs(B)
	    quotient = 0
	    temp = 0
	    
	    for i in range(31,-1,-1):
	        if temp+(B<<i) <= A:
	            temp += B<<i
	            quotient |= 1<<i
	    
	    if sign*quotient <= 2147483647:
	        return sign*quotient
	    else:
	        return sign*2147483647