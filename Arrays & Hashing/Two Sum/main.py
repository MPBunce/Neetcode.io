#Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        toReturn = [0,1]
        
        if len(nums) == 2:
            return toReturn
        
        for i in range( len(nums) ):
            for j in range( i + 1, len(nums)):
                
                if i == j:
                    pass
                
                sum = nums[i] + nums[j]
                
                if sum == target:
                    toReturn[0] = i
                    toReturn[1] = j
                    return toReturn
         
#Hash Map One Pass

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        table={}
        
        for index,num in enumerate(nums):
            
            complement=target-num
            
            if complement in table:
                
                return [index,table[complement]]
            
            else:
                
                table[num]=index
                    
        return []