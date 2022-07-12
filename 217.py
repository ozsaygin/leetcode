class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    
    
        d = {}
        len_nums = len(nums)
        for i in range(len_nums):
            if nums[i] not in d: 
                d[nums[i]] = 0
                
            d[nums[i]] += 1
            
        for k, v in d.items(): 
            if v > 1: 
                return True
            
        return False