# Range Sum
# Problem Description
# Given two integers A and B such that A <= B. A Function F is defined as follows:
# F[0] = 0
# F[1] = 1
# F[n] = F[n-1] + F[n-2]; n > 1
# Function S(A, B) = F[A] + F[A+1] + F[A+2] + ... + F[B]. Find and return S(A, B) modulo (109+7).  

# Problem Constraints
# 0 <= A <= B <= 109

# Input Format
# The arguments given are two integers A and B.

# Output Format
# Return an integer denoting the value of S(A, B) modulo (109+7).

# Example Input
# Input 1:
#  A = 0
#  B = 3
# Input 2:
#  A = 3
#  B = 4

# Example Output
# Output 1:
#  4
# Output 2:
#  5

# Example Explanation
# Explanation 1:
#  F(0) = 0, F(1) = 1, F(2) = 1, F(3) = 2.
#  S(0, 3) = F(0) + F(1) + F(2) + F(3) = 0 + 1 + 1 + 2 = 4.
# Explanation 2:
#  F(3) = 2, F(4) = 3.
#  S(3, 4) = F(3) + F(4) = 2 + 3 = 5.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        # import math
        # phi = (1+math.sqrt(5))/2
        # def fib_nth(x):
        #     return round(phi**x/math.sqrt(5))
        # fib_sum = fib_nth(B+2) - fib_nth(A+1)
        # print(fib_sum)
        # return fib_sum%1000000007
        
        init_matrix = [[1,1],[1,0]]
        
        P = None
        Q = None
        
        if A-1>=1:
            P = self.power(init_matrix, A-1)
            fib_A = (P[0][0]%1000000007 + P[1][0]%1000000007)%1000000007
        else:
            fib_A = 1
            
        if B>=1:
            if P:
               Q = self.matrix_multiply(P, self.power(init_matrix, B-A+1))
            else:
                Q = self.power(init_matrix, B)
            fib_B = (Q[0][0]%1000000007 + Q[1][0]%1000000007)%1000000007
        else:
            fib_B = 0
            
        return (fib_B%1000000007-fib_A%1000000007)%1000000007
        
    def matrix_multiply(self, X, Y):
        A_00 = ((X[0][0]%1000000007)*(Y[0][0]%1000000007) + (X[0][1]%1000000007)*(Y[1][0]%1000000007))
        A_01 = ((X[0][0]%1000000007)*(Y[0][1]%1000000007) + (X[0][1]%1000000007)*(Y[1][1]%1000000007))
        A_10 = ((X[1][0]%1000000007)*(Y[0][0]%1000000007) + (X[1][1]%1000000007)*(Y[1][0]%1000000007))
        A_11 = ((X[1][0]%1000000007)*(Y[0][1]%1000000007) + (X[1][1]%1000000007)*(Y[1][1]%1000000007))
        return [[A_00%1000000007, A_01%1000000007],[A_10%1000000007, A_11%1000000007]]
    
    def power(self, A, B):
        if B==1:
            return A
        answer = self.power(A,B//2)
        answer = (self.matrix_multiply(answer,answer))
        if B%2==1:
            answer = (self.matrix_multiply(answer,A))
        return answer