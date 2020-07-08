# Aggressive cows

# Problem Description
# Farmer John has built a new long barn, with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall, and an integer B which represent the number of cows.
# His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance?

# Problem Constraints
# 2 <= N <= 100000
# 0 <= A[i] <= 109
# 2 <= B <= N

# Input Format
# The first argument given is the integer array A.
# The second argument given is the integer B.

# Output Format
# Return the largest minimum distance possible among the cows.

# Example Input

# Input 1:
# A = [1, 2, 3, 4, 5]
# B = 3

# Input 2:
# A = [1, 2]
# B = 2

# Example Output

# Output 1:
#  2

# Output 2:
#  1

# Example Explanation

# Explanation 1: 
# John can assign the stalls at location 1,3 and 5 to the 3 cows respectively.
# So the minimum distance will be 2.

# Explanation 2: 
# The minimum distance will be 1.

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        # A.sort()
        # low = 0
        # high = max(A)-min(A)
        # ans = 0
        
        # def possibe(A, B, mid):
        #     last_pos = A[0]
        #     cows_placed = 1
            
        #     for i in range(1,len(A)):
        #         if(A[i]-last_pos >= mid):
        #             cows_placed += 1
        #             if cows_placed == B:
        #                 return True
        #             last_pos = A[i]
        
        #     if cows_placed >= B:
        #         return True
        #     else:
        #         return False
        
        # while low < high:
            
        #     mid = low + (high-low)//2
            
        #     if(possibe(A, B, mid)):
        #         ans = mid
        #         low = mid+1
        #     else:
        #         high = mid
        
        # return ans
        
        
        # def pre_compute(A, B, mid):
        #     count = 1
        #     n = len(A)
            
        #     pos = 0
        #     i = 0
        #     while i<n:
        #         if A[i] - A[pos] >= mid:
        #             count+=1
        #             pos = i
        #         if count == B:
        #             return True
        #         i+=1
        #     return False
            
        
        # l = 1
        # h = max(A)-min(A)
        # A.sort()
        
        # while l <= h:
        #     mid = l + (h-l)//2
        #     temp = pre_compute(A, B, mid)
        #     # print(mid)
        #     if temp == True:
        #         ans = mid
        #         l = mid + 1
        #     else:
        #         h = mid - 1
        
        # return ans
        
        A = list(sorted(A))
        lo = 0
        hi = A[0] + A[-1] + 1
        
        while lo < hi:
            mid = (hi + lo) // 2
            
            if self.F(A, B, mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1
    
    def F(self, A, B, mid):
        prev = A[0]
        cow = 1
        for i in range(1, len(A)):
            diff = A[i] - prev
            
            if diff >= mid:
                cow += 1
                if cow == B:
                    return 1
                prev = A[i]
        return 0