# ZigZag Level Order Traversal BT

# Problem Description
# Given a binary tree, return the zigzag level order traversal of its nodes values. (ie, from left to right, then right to left for the next level and alternate between).

# Problem Constraints
# 1 <= number of nodes <= 10^5

# Input Format
# First and only argument is root node of the binary tree, A.

# Output Format
# Return a 2D integer array denoting the zigzag level order traversal of the given binary tree.

# Example Input

# Input 1:
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Input 2:
#    1
#   / \
#  6   2
#     /
#    3

# Example Output

# Output 1:
#  [
#    [3],
#    [20, 9],
#    [15, 7]
#  ]

# Output 2:
#  [ 
#    [1]
#    [2, 6]
#    [3]
#  ]

# Example Explanation

# Explanation 1:
#  Return the 2D array. Each row denotes the zigzag traversal of each level.

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def zigzagLevelOrder(self, A):
	    
	   # ans_arr = []
	   # ltr = True
	   # prev_level = [A]
	    
	   # while prev_level:
	   #     curr_vals = [p.val for p in prev_level]
	   #     ans_arr.append(curr_vals if ltr else curr_vals[::-1])
	        
	   #     next_level = []
	   #     for p in prev_level:
	   #         next_level.append(p.left)
	   #         next_level.append(p.right)
	        
	   #     prev_level = [p for p in next_level if p]
	   #     ltr = not ltr
	        
	   # return ans_arr
	   
	   from queue import Queue
	   
	   ans = []
	   
	   if not A:
	       return ans
	   
	   q = Queue()
	   q.put(A)
	   N = 1
	   odd_level = True
	   
	   while not q.empty():
	       temp = 0
	       level_nodes = []
	       
	       for i in range(N):
	           node = q.get()
	           level_nodes.append(node.val)
	           
	           if node.left:
	               temp+=1
	               q.put(node.left)
	           if node.right:
	               temp+=1
	               q.put(node.right)
	               
	       N = temp
	       if odd_level:
	           ans.append(level_nodes)
	       else:
	           ans.append(list(reversed(level_nodes)))
	           
	       odd_level = not odd_level
	       
	   return ans