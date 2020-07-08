# Smallest Good Base

# Given an integer A, we call k >= 2 a good base of A, if all digits of A base k are 1. Now given a string representing A, you should return the smallest good base of A in string format.

# Input Format
# The only argument given is the string representing A.

# Output Format
# Return the smallest good base of A in string format.

# Constraints
# 3 <= A <= 10^18

# For Example

# Input 1:
#     A = "13"
# Output 1:
#     "3"     (13 in base 3 is 111)

# Input 2:
#     A = "4681"
# Output 2:
#     "8"     (4681 in base 8 is 11111).

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        
        n = int(A)
        for i in range(31,0,-1):
            low = 2
            high = n-1
            while low<=high:
                m = (low+high)//2
                sum = (pow(m,i)-1)//(m-1)
                if sum==n:
                    return str(m)
                elif sum>n:
                    high = m-1
                else:
                    low = m+1