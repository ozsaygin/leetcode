import collections 
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        nums_to_freqs = collections.Counter(nums)
        freq_to_nums = {}

        for num, freq in nums_to_freqs.items(): 
            if freq not in freq_to_nums: 
                freq_to_nums[freq] = [] 

            freq_to_nums[freq].append(num)

        freqs = freq_to_nums.keys()
        freqs = [-freq for freq in freqs]
        heapq.heapify(freqs)

        k_freq_nums = [] 
        while len(k_freq_nums) < k: 
            freq = -1 * heapq.heappop(freqs)
            for num in freq_to_nums[freq]:
                k_freq_nums.append(num)
                if len(k_freq_nums) >= k:
                    break

        return k_freq_nums
