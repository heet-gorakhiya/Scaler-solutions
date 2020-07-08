# N/3 Repeat Number

# You're given a read only array of n integers. Find out if any integer occurs more than n/3 times in the array in linear time and constant additional space.

# If so, return the integer. If not, return -1.

# If there are multiple solutions, return any one.

# Example :

# Input : [1 2 3 1 1]

# Output : 1 
# 1 occurs 3 times which is more than 5/3 times.

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        
        ME_1 = None
        ME_2 = None
        count1 = 0
        count2 = 0
        
        for i in range(len(A)):
            if not ME_1:
                ME_1 = A[i]
                count1 += 1
                continue
            if not ME_2:
                if A[i] != ME_1:
                    ME_2 = A[i]
                    count2 += 1
                    continue
                else:
                    count1 += 1
                    continue
            
            if A[i] == ME_1:
                count1 += 1
            elif A[i] == ME_2:
                count2 += 1
            elif A[i] != ME_1 and A[i] != ME_2:
                if count1 == 0:
                    ME_1 = A[i]
                    count1 += 1
                elif count2 == 0:
                    ME_2 = A[i]
                    count2 += 1
                else:
                    count1 -= 1
                    count2 -= 1
        
        cnt_1 = cnt_2 = 0
        for i in range(len(A)):
            if ME_1 == A[i]:
                cnt_1 += 1
            if ME_2 == A[i]:
                cnt_2 += 1
                
        if cnt_1 > len(A)/3:
            return ME_1
        elif cnt_2 > len(A)/3:
            return ME_2
        else:
            return -1