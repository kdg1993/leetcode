class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            num_a = nums[i]
            num_b = nums[i+1]
            if num_a > num_b:
                return num_b
        
        return nums[0]