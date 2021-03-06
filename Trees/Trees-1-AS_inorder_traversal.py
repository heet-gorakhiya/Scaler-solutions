# Inorder Traversal

# Problem Description
# Given a binary tree, return the inorder traversal of its nodes values.

# NOTE: Using recursion is not allowed.

# Problem Constraints
# 1 <= number of nodes <= 10^5

# Input Format
# First and only argument is root node of the binary tree, A.

# Output Format
# Return an integer array denoting the inorder traversal of the given binary tree.

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
#  [1, 3, 2]

# Output 2:
#  [6, 1, 3, 2]


# Example Explanation

# Explanation 1:
#  The Inorder Traversal of the given tree is [1, 3, 2].

# Explanation 2:
#  The Inorder Traversal of the given tree is [6, 1, 3, 2].

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def inorderTraversal(self, A):
        
        from queue import LifoQueue
        
        # Recursive solution
        
        # if not A:
        #     return
        # self.inorderTraversal(A.left)
        # # ans_arr.append(A.val)
        # print(A.val)
        # self.inorderTraversal(A.right)
        
        # Iterative Solution using stack
        
        curr_node = A
        ans_arr = []
        stack = LifoQueue()
        
        while True:
            if curr_node:
                stack.put(curr_node)
                curr_node = curr_node.left
            else:
                if not stack.empty():
                    temp = stack.get()
                    ans_arr.append(temp.val)
                    curr_node = temp.right
                else:
                    return ans_arr