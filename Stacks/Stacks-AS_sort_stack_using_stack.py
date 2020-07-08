# Sort stack using another stack

# Problem Description
# Given a stack of integers A, sort it using another stack.
# Return the array of integers after sorting the stack using another stack.

# Problem Constraints
# 1 <= |A| <= 5000
# 0 <= A[i] <= 1000000000

# Input Format
# The only argument given is the integer array A.

# Output Format
# Return the array of integers after sorting the stack using another stack.

# Example Input

# Input 1:
#  A = [5, 4, 3, 2, 1]

# Input 2:
#  A = [5, 17, 100, 11]

# Example Output

# Output 1:
#  [1, 2, 3, 4, 5]

# Output 2:
#  [5, 11, 17, 100]

# Example Explanation

# Explanation 1:
#  Just sort the given numbers.

# Explanation 2:
#  Just sort the given numbers.

from queue import LifoQueue
import copy

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        
        # return list(sorted(A)) # Just simple sorting will also suffice
        # But we need to implement using stack.
        
        def top(stack):
            ans = stack.get()
            temp = copy.deepcopy(ans)
            stack.put(temp)
            return ans
        
        ans_stack = LifoQueue()
        helper_stack_1 = LifoQueue()
        helper_stack_2 = LifoQueue()
        # curr_num = -10**15
        
        for i in A:
            helper_stack_1.put(i)
        
        # itr = 0
        while ans_stack.qsize() < len(A):
            # if itr == 0:
                # ans_stack.put(helper_stack_1.get())
            curr_num = helper_stack_1.get()
            if ans_stack.empty():
               ans_stack.put(curr_num)
            else:
                # top_ans = ans_stack.get()
                top_ans = top(ans_stack)
                if top_ans <= curr_num:
                    # ans_stack.put(top_ans) --del
                    ans_stack.put(curr_num)
                else:
                    # helper_stack_2.put(top_ans)
                    while True:
                        if top(ans_stack) < curr_num:
                            ans_stack.put(curr_num)
                            while not helper_stack_2.empty():
                                ans_stack.put(helper_stack_2.get())
                            break
                        else:
                            helper_stack_2.put(ans_stack.get())
                            break
        
        ans_arr = []
        while not ans_stack.empty():
            ans_arr.append(ans_stack.get())
            
        return ans_arr