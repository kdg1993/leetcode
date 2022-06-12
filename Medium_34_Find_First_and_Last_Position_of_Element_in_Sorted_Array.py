class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        idx_start = -1
        idx_end = -1
        
        cnt = 0
        for idx, num in enumerate(nums):
            if num == target and cnt == 0:
                idx_start = idx
                idx_end = idx
                cnt = 1
            elif num == target and cnt != 0:
                idx_end = idx
                
        return [idx_start, idx_end] 