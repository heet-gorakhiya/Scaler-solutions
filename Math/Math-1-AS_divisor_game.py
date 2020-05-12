# Divisor game
# Problem Description
# Scooby has 3 three integers A, B and C. Scooby calls a positive integer special if it is divisible by B and it is divisible by C. You need to tell number of special integers less than or equal to A.     

# Problem Constraints
# 1 <= A, B, C <= 109

# Input Format
# First argument is a positive integer A
# Second argument is a positive integer B
# Third argument is a positive integer C

# Output Format
# One integer corresponding to the number of special integers less than or equal to A.

# Example Input
# Input 1:
#  A = 12
#  B = 3
#  C = 2
# Input 2:
#  A = 6
#  B = 1
#  C = 4

# Example Output
# Output 1:
#  2
# Output 2:
#  1

# Example Explanation
# Explanation 1:
#  The two integers divisible by 2 and 3 and less than or equal to 12 are 6,12.
# Explanation 2:
#  Only 4 is a positive integer less than equal to 6 which is divisible by 1 and 4.

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        
        def gcd(x, y):
            if y==0:
                return abs(x)
            else:
                return gcd(y, x%y)
        
        gcd_BC = gcd(B,C)
        lcm_BC = (B*C)//gcd_BC
        
        count = 0
        for i in range(1,A):
            if i*lcm_BC <= A:
                count += 1
            else:
                break
        
        return count