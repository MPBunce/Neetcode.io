#Brute Force double loop 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range( len(nums) ):
            for j in range(i+1, len(nums) ):
                sum = nums[i] + nums[j]
                if sum == target:
                    return[i, j]
                

#On dict solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        new_dict = {}
        
        for i in range( len(nums) ):
            pairVal = target - nums[i]
            if pairVal in new_dict:
                return [ new_dict[pairVal], i ]
            else:
                new_dict[ nums[i] ] = i