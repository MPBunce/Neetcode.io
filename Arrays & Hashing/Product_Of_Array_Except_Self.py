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
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        prefix = 1
        postfix = 1

        for i in range( length ):
            res[i] = prefix
            prefix *= nums[i]

        for i in range( length-1, -1, -1 ):
            res[i] *= postfix
            postfix *= nums[i]

        return res

