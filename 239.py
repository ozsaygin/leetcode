import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        output = [] 
        q = collections.deque()
        l = r = 0

        while r < len(nums): 
            # pop smaller values from q 
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k: 
                output.append(nums[q[0]])
                l += 1
                
            r += 1
            
        return output
        
#         Q = [] 
#         q_size = 0
#         window_max_arr = []
#         len_nums = len(nums)

#         for i in range(0, len_nums-k+1):
            
#             window = nums[i:i+k]
#             for j in range(k):
#                 elm = window[j]
                
#                 if not Q:
#                     Q.append(elm)
#                     q_size += 1
#                     continue

#                 # elm to be inserted
#                 while Q and Q[0] <= elm:
#                     # pop the top if new elm is greater
#                     Q.pop(0)
#                     q_size -= 1
                    
#                 Q.append(elm)
#                 q_size += 1
                
#                 while q_size > k: 
#                     Q.pop(0)
#                     q_size -= 1
                    
#             window_max_arr.append(Q[0])
        
#         return window_max_arr
