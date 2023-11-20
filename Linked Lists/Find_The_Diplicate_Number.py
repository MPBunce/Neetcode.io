class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        x = set()

        for n in nums:
            if n in x:
                return n
            else:
                x.add(n)