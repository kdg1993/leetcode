class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:       
        l = len(nums)
        nums.sort()
        print(nums)
        possible = []
        
        for i in range(l-2):
            if nums[i] > 0:
                break
            
            j = i + 1
            k = l - 1
            
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if temp == 0:
                    possible.append((nums[i], nums[j], nums[k]))
                    j += 1
                elif temp < 0:
                    j += 1
                else:
                    k += -1
        
        return set(possible)