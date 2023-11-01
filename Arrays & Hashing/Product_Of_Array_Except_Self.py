#Time Limit Error
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range( len(nums) ):
            sum = 1
            for j in range( len(nums) ):

                if i != j:
                    sum = sum * nums[j]
                
            res.append(sum)

        return res

#O(n) solution 

