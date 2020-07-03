# Level Order

# Problem Description
# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

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
#    [9, 20],
#    [15, 7]
#  ]

# Output 2:
#  [ 
#    [1]
#    [6, 2]
#    [3]
#  ]

# Example Explanation

# Explanation 1:
#  Return the 2D array. Each row denotes the traversal of each level.

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def levelOrder(self, A):
	    
	    from queue import Queue
	    ans = []
	    
	    if not A:
	        return ans
	    
	    q = Queue()
	    q.put(A)
	    N = 1
	    
	    while not q.empty():
	        temp = 0
	        level_nodes = []
	        
	        for i in range(N):
	            node = q.get()
	            
	            level_nodes.append(node.val)
	            
	            if node.left:
	                temp += 1
	                q.put(node.left)
	            if node.right:
	                temp += 1
	                q.put(node.right)
	        N = temp
	        ans.append(level_nodes)
	    
	    return ans


# def lvlord_traversal(root):
#     '''
#     Function to implement Level-Order Traversal in a given binary tree
#     '''
#     from queue import Queue
#     # Instantiate Queue
#     traversal_q = Queue()
#     traversal_q.put(root)
#     ans_arr = []
#     # Null check
#     if not root:
#         return
#     # Loop while Queue is not empty
#     while not traversal_q.empty():
#         # Add root 
#         root = traversal_q.get()
#         # Print value
#         ans_arr.append(root.data)
#         # Add left and right nodes to Queue
#         if root.left:
#             traversal_q.put(root.left)
#         if root.right:
#             traversal_q.put(root.right)
    
#     return ans_arr