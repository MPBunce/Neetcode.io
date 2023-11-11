class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for List in matrix:
            l,r = 0, len(List)-1

            while l <= r:
                m = (l+r) // 2
                if List[m] > target:
                    r = m - 1
                elif List[m] < target:
                    l = m + 1
                else:
                    return True
        
        return False