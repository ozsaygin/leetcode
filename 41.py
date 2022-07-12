class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # replace negative integers with zero
        # negative integers have no meaning for this problem
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        # iterate over nums 
        for i in range(len(nums)):
            
            # if num is greater than array size
            # it have no meaning
            num_idx = abs(nums[i]) - 1
            if num_idx >= len(nums) or num_idx < 0: 
                continue            
            
            # if num has an index in array 
            # negate its index value if not 
            if nums[num_idx] >= 0: 
                
                nums[num_idx] = - nums[num_idx]

                if nums[num_idx] == 0:
                    nums[num_idx] = - (len(nums) + 1)
       
        for i in range(len(nums)):
            if nums[i] < 0: 
                continue

            return i+1

        return len(nums) + 1

