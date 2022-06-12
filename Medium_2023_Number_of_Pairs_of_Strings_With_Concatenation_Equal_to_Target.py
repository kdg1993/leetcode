class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        from itertools import combinations, permutations
    
        cnt = 0
        for i, j in combinations(nums, 2):
            if i+j == target:
                cnt += 1
            if j+i ==  target:
                cnt += 1
                
        return cnt