# Odd and Even Levels

# Problem Description
# Given a binary tree of integers. Find the difference between the sum of nodes at odd level and sum of nodes at even level.
# NOTE: Consider the level of root node as 1.

# Problem Constraints
# 1 <= Number of nodes in binary tree <= 100000
# 0 <= node values <= 10^9

# Input Format
# First and only argument is a root node of the binary tree, A

# Output Format
# Return an integer denoting the difference between the sum of nodes at odd level and sum of nodes at even level.

# Example Input

# Input 1:
#         1
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7
#   /
#  8 

# Input 2:
#         1
#        / \
#       2   10
#        \
#         4


# Example Output

# Output 1:
#  10

# Output 2:
#  -7


# Example Explanation

# Explanation 1:
#  Sum of nodes at odd level = 23
#  Sum of ndoes at even level = 13

# Explanation 2:
#  Sum of nodes at odd level = 5
#  Sum of ndoes at even level = 12

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):
        
        from queue import Queue
        
        ans = 0
        
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
                ans += sum(level_nodes)
            else:
                ans -= sum(level_nodes)
               
            odd_level = not odd_level
           
        return ans