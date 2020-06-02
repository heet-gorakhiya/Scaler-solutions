# Closest MinMax

# Problem Description
# Given an array A. Find the size of the smallest subarray such that it contains atleast one occurrence of the maximum value of the array
# and atleast one occurrence of the minimum value of the array.

# Problem Constraints
# 1 <= |A| <= 2000

# Input Format
# First and only argument is vector A

# Output Format
# Return the length of the smallest subarray which has atleast one occurrence of minimum and maximum element of the array

# Example Input

# Input 1:
# A = [1, 3]

# Input 2:
# A = [2]

# Example Output

# Output 1:
#  2
# Output 2:
#  1

# Example Explanation

# Explanation 1:
#  Only choice is to take both elements.

# Explanation 2:
#  Take the whole array.

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        
        if len(A) < 3:
            return len(A)
        
        max_element = max(A)
        min_element = min(A)
        min_arr = []
        max_arr = []
        ans = 10**15
        
        for i in range(len(A)):
            if A[i] == min_element:
                min_arr.append(i)
            if A[i] == max_element:
                max_arr.append(i)
                
        for i in range(len(max_arr)):
            for j in range(len(min_arr)):
                if abs(max_arr[i]-min_arr[j])+1 < ans:
                    ans = abs(max_arr[i]-min_arr[j])+1
                
        return ans