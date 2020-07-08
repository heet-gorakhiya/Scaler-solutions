# Closest pair from sorted arrays

# Problem Description
# Given two sorted arrays of distinct integers, A and B, and an integer C, find and return the pair whose sum is closest to C and the pair has one element from each array.
# More formally, find A[i] and B[j] such that abs((A[i] + B[j]) - C) has minimum value.
# If there are multiple solutions find the one with minimum i and even if there are multiple values of j for the same i then return the one with minimum j.
# Return an array with two elements {A[i], B[j]}.

# Problem Constraints
# 1 <= length of both the arrays <= 100000
# 1 <= A[i], B[i] <= 109
# 1 <= C <= 109

# Input Format
# The first argument given is the integer array A.
# The second argument given is the integer array B.
# The third argument given is integer C.

# Output Format
# Return an array of size 2 denoting the pair which has sum closest to C.

# Example Input

# Input 1:
#  A = [1, 2, 3, 4, 5]
#  B = [2, 4, 6, 8]
#  C = 9

# Input 2:
#  A = [5, 10, 20]
#  B = [1, 2, 30]
#  C = 13

# Example Output

# Output 1:
#  [1, 8]

# Output 2:
#  [10, 2]

# Example Explanation

# Explanation 1:
#  There are three pairs: (1, 8), (3, 6), (5, 4), that gives the minimum value.
#  Since we have to return the value with minimum i and then with minimum j. We will return [1, 8].

# Explanation 2:
#  [10, 2] is the only pair such abs(10+2-13) is minimum.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        
        # i = 0
        # j = len(B)-1
        # closest_sum = 10**15
        # p1 = 0
        # p2 = 0
        
        # while i < len(A) or j >= 0:
        #     print(i,j)
        #     print(A[i],B[j])
        #     curr_sum = abs(A[i]+B[j]-C)
        #     print(curr_sum)
        #     if curr_sum < closest_sum:
        #         p1 = i
        #         p2 = j
        #         closest_sum = curr_sum
        #         print("new closest sum : ", closest_sum)
        #     # if curr_sum > closest_sum:
        #     #     i+=1
        #     # elif curr_sum < closest_sum:
        #     #     p1 = i
        #     #     p2 = j
        #     #     j-=1
        #     elif curr_sum == closest_sum:
        #         if i == p1:
        #             j = p2
        #         # return [A[i],B[j]]
        #     # elif curr_sum == 0:
        #     #     return [A[i],B[j]]
                
        #     if A[i]+B[j]<C:
        #         i+=1
        #     else:
        #         j-=1
                
        # return [A[p1],B[p2]]
        
        lA = len(A)
        lB = len(B)
        i = 0
        j = lB-1
        ans = 999999999
        ans_i = lA-1
        ans_j = lB-1
        while i < lA and j >= 0:
            temp = A[i] + B[j]
            curr = abs(temp - C)
            if (curr < ans) or (curr == ans and ans_j > j and ans_i == i):
                ans_i = i
                ans_j = j
                ans = curr
                
            if temp < C:
                i += 1
            else:
                j -= 1
                
        return [A[ans_i], B[ans_j]]