# Spiral Order Matrix II

# Problem Description
# Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order.

# Problem Constraints
# 1 <= A <= 1000

# Input Format
# First and only argument is integer A

# Output Format
# Return a 2-D matrix which consists of the elements in spiral order.

# Example Input

# Input 1:
# 1

# Input 2:
# 2

# Example Output

# Output 1:
# [ [1] ]

# Output 2:
# [ [1, 2], [4, 3] ]

# Example Explanation

# Explanation 1: 
# Only 1 is to be arranged.

# Explanation 2:
# 1 --> 2
#       |
#       |
# 4<--- 3


class Solution:
	# @param A : integer
	# @return a list of list of integers
	def generateMatrix(self, A):
	    
	    matrix = [[0 for i in range(A)] for j in range(A)]
	    row_start = 0
	    row_end = A-1
	    col_start = 0
	    col_end = A-1
	    direction = 0
	    num = 1
	    
	    while row_start <= row_end and col_start <= col_end:
	        if direction == 0:
	            for i in range(col_start, col_end+1):
	                matrix[row_start][i] = num
	                num += 1
	            row_start+=1
            
            elif direction == 1:
                for i in range(row_start, row_end+1):
                    matrix[i][col_end] = num
                    num+=1
                col_end -= 1
            
            elif direction == 2:
                for i in range(col_end, col_start-1, -1):
                    matrix[row_end][i] = num
                    num+=1
                row_end-=1
            
            elif direction == 3:
                for i in range(row_end, row_start-1, -1):
                    matrix[i][col_start] = num
                    num+=1
                col_start+=1
                
            direction = (direction+1)%4
            
        return matrix