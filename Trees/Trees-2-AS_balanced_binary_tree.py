# Balanced Binary Tree

# Problem Description
# Given a root of binary tree A, determine if it is height-balanced.
# A height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

# Problem Constraints
# 1 <= size of tree <= 100000

# Input Format
# First and only argument is the root of the tree A.

# Output Format
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem.

# Example Input

# Input 1:
#     1
#    / \
#   2   3

# Input 2: 
#        1
#       /
#      2
#     /
#    3

# Example Output

# Output 1:
# 1

# Output 2:
# 0

# Example Explanation

# Explanation 1:
# It is a complete binary tree.

# Explanation 2:
# Because for the root node, left subtree has depth 2 and right subtree has depth 0. 
# Difference = 2 > 1. 

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class TreeInfo:
    def __init__(self, height, is_balanced):
        self.height = height
        self.is_balanced = is_balanced

class Solution:
	# @param A : root node of tree
	# @return an integer
	def isBalanced(self, A):
	    
	    def check_balanced(root):
	        
	        if not root:
	            return TreeInfo(-1, True)
	        
	        lst_info = check_balanced(root.left)
	        
	        if lst_info.is_balanced:
	            
	            rst_info = check_balanced(root.right)
	            
	            if rst_info.is_balanced and abs(rst_info.height - lst_info.height) <= 1:
	                
	                return TreeInfo(max(rst_info.height, lst_info.height)+1, True)
	                
	            else:
	                return TreeInfo(-1, False)
	        else:
	            return TreeInfo(-1, False)
	        
	    ans_obj = check_balanced(A)
	    
	    if ans_obj.is_balanced:
	        return 1
	    else:
	        return 0