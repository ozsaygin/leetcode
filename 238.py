class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        len_nums = len(nums)
        
        left_product_nums = len_nums*[0]
        right_product_nums = len_nums*[0]
        
        len_nums = len(nums)
        
        left_product_nums[0] = nums[0]
        for i in range(1, len_nums):
            left_product_nums[i] = nums[i] * left_product_nums[i-1]
            
        right_product_nums[len_nums-1] = nums[len_nums-1]
        for i in range(len_nums-2, -1, -1): 
            right_product_nums[i] = nums[i] * right_product_nums[i+1]
            
        print(left_product_nums)
        print(right_product_nums)
        
        out = len_nums * [0]
        out[0] = right_product_nums[1]
        out[len_nums-1] = left_product_nums[len_nums-2]
        for i in range(1, len_nums-1):
            out[i] = left_product_nums[i-1] * right_product_nums[i+1]
          
        
        return out