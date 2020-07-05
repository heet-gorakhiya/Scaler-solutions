# Left view of binary tree

# Problem Description
# Given a binary tree of integers. Return an array of integers representing the left view of the Binary tree.
# Left view of a Binary Tree is a set of nodes visible when the tree is visited from Left side
# NOTE: The value comes first in the array which have lower level.

# Problem Constraints
# 1 <= Number of nodes in binary tree <= 100000
# 0 <= node values <= 10^9

# Input Format
# First and only argument is a root node of the binary tree, A.

# Output Format
# Return an integer array denoting the left view of the Binary tree.

# Example Input

# Input 1:
#             1
#           /   \
#          2    3
#         / \  / \
#        4   5 6  7
#       /
#      8 

# Input 2:
#             1
#            /  \
#           2    3
#            \
#             4
#              \
#               5

# Example Output

# Output 1:
#  [1, 2, 4, 8]

# Output 2:
#  [1, 2, 4, 5]

# Example Explanation

# Explanation 1:
#  The Left view of the binary tree is returned.

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        
        from queue import Queue
        ans = []
        # q = []
        
        if not A:
            return ans
        
        q = Queue()
        q.put(A)
        N = 1
        
        while not q.empty():
            temp = 0
            # level_nodes = []
            
            for i in range(N):
                node = q.get()
                
                # level_nodes.append(node.val)
                if i == 0:
                    ans.append(node.val)
                
                if node.left:
                    temp += 1
                    q.put(node.left)
                if node.right:
                    temp += 1
                    q.put(node.right)
            N = temp
            # ans.append(level_nodes[0])
        
        return ans