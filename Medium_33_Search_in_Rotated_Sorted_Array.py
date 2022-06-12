class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pt = -1
        for idx, num in enumerate(nums):
            if num == target:
                pt = idx
                
        return pt