class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        trgt_in = False
        
        if target > matrix[-1][-1]:
            return False
        
        for row in matrix:
            if target > row[-1]:
                continue
            for num in row:
                if num == target:
                    trgt_in = True
                    break
        
        return trgt_in