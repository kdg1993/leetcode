class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        idx_max = 0
        num_max = nums[0]
        for idx, num in enumerate(nums):
            if num > num_max:
                idx_max = idx
                num_max = num
            
        return idx_max