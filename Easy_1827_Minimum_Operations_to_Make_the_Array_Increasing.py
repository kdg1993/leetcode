class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Obivous case division branch
        if len(nums) == 1:
            return 0
        else:
            cnt = 0 # Increment count
            for i in range(1, len(nums)):
                diff = nums[i] - nums[i-1]
                if diff > 0: # if increment is not needed
                    continue
                else:
                    cnt += -diff + 1 # Check increment counts
                    nums[i] += -diff + 1
            return cnt