# Postorder Traversal

# Problem Description
# Given a binary tree, return the Postorder traversal of its nodes values.
# NOTE: Using recursion is not allowed.

# Problem Constraints
# 1 <= number of nodes <= 10^5

# Input Format
# First and only argument is root node of the binary tree, A.

# Output Format
# Return an integer array denoting the Postorder traversal of the given binary tree.

# Example Input

# Input 1:
#    1
#     \
#      2
#     /
#    3

# Input 2:
#    1
#   / \
#  6   2
#     /
#    3

# Example Output

# Output 1:
#  [3, 2, 1]

# Output 2:
#  [6, 3, 2, 1]

# Example Explanation

# Explanation 1:
#  The Preoder Traversal of the given tree is [3, 2, 1].

# Explanation 2:
#  The Preoder Traversal of the given tree is [6, 3, 2, 1].

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def postorderTraversal(self, A):
	    
	    from queue import LifoQueue
	    
	    stack = LifoQueue()
	    stack.put(A)
	    ans_arr = []
	    
	    while not stack.empty():
	        curr_node = stack.get()
	        ans_arr.append(curr_node.val)
	        if curr_node.left:
	            stack.put(curr_node.left)
	        if curr_node.right:
	            stack.put(curr_node.right)
	            
	    return list(reversed(ans_arr))