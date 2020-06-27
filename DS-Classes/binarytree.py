# File Description : Class for Tree Node and Utilities like travsersal, etc.

from queue import Queue, LifoQueue
from collections import OrderedDict

class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class TreeUtils:
    def __init__(self, rootnode):
        '''
        Init function
        '''
        self.root = rootnode

    def traversal(self, root, tr_type='preorder'):
        '''
        Function for the recusrsive traversal of a tree, given a root node and traversal type.
        '''
        if not root:
            return 0
        
        if tr_type == 'preorder':
            print(root.data)
            self.traversal(root.left, tr_type='preorder')
            self.traversal(root.right, tr_type='preorder')
        
        elif tr_type == 'inorder':
            self.traversal(root.left, tr_type='inorder')
            print(root.data)
            self.traversal(root.right, tr_type='inorder')
        
        elif tr_type == 'postorder':
            self.traversal(root.left, tr_type='postorder')
            self.traversal(root.right, tr_type='postorder')
            print(root.data)
        
        else:
            print("Incorrect traversal type!")
            return -1

    # !!! Function is incomplete
    def traversal_itr(self, root, ans_arr, tr_type='preorder'):
        '''
        Function for the iterative traversal of a tree, given a root node and traversal type.
        '''
        stack = LifoQueue()
        
        while root:
            
            if tr_type == 'preorder':
                
                ans_arr.append(root.data)
                while root.left:
                    break
                
            elif tr_type == 'inorder':
                pass
            elif tr_type == 'postorder':
                pass
            else:
                pass
        
        for i in ans_arr:
            print(i)
            
        return ans_arr
    
    def lvlord_traversal(root):
        '''
        Function to implement Level-Order Traversal in a given binary tree
        '''
        # Instantiate Queue
        traversal_q = Queue()
        traversal_q.put(root)
        ans_arr = []
        # Null check
        if not root:
            return
        # Loop while Queue is not empty
        while not traversal_q.empty():
            # Add root 
            root = traversal_q.get()
            # Print value
            ans_arr.append(root.data)
            # Add left and right nodes to Queue
            if root.left:
                traversal_q.put(root.left)
            if root.right:
                traversal_q.put(root.right)
        
        return ans_arr

    def vert_traversal(root):
        '''
        This function prints the Vertical Order Traversal given the root node of a tree
        '''
        # Initialize necessary variables
        dist_dict = {}
        distance = 0
        # Nested function that recursively generates node data hashmap
        def generate_map(root, dist_dict, distance):
            # Null case
            if not root:
                return
            # If there are multiple nodes at same horizontal distance 
            if distance in dist_dict:
                # Append the node's data into string corresponding to existing key
                dist_dict[distance] += ","+str(root.data)
            else:
                # Create new key and add node data as its value
                dist_dict[distance] = str(root.data)
            # Recursion over child nodes
            generate_map(root.left, dist_dict, distance-1)
            generate_map(root.right, dist_dict, distance+1)
        
        # Call the nested function in the outer function 
        generate_map(root, dist_dict, distance)
        # Extract keys (distance values) and sort them
        keys_list = list(sorted(dist_dict.keys()))
        ans_arr = []
        # Create answer array in ascending order of distance 
        for key in keys_list:
            # Data of multiple nodes added into ans_arr order-wise (L=>R) 
            vals = dist_dict[key].split(",")
            ans_arr.extend(vals)
        # Typecast all values to int
        ans_arr = [ int(i) for i in ans_arr ]
        
        return ans_arr