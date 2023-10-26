#Time Limit Error
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range( len(nums) ):
            for j in range(i+1, len(nums) ):
                
                if nums[i] == nums[j]:
                    return True
        
        return False
    
#Hash Map Time Accepted

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_dict = {}
        for i in range(len(nums)):

            if nums[i] in new_dict:
                if new_dict[nums[i]] == 1:
                    return True
                new_dict[nums[i]] += 1
            else:
                new_dict[nums[i]] = 1
                
        return False

#Another Hash Map Solution

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
    
        dic = {}
    
        for i in range(len(nums)):
            dic[ nums[i] ] = 1 + dic.get(nums[i], 0)
            if dic[ nums[i] ] > 1:
                return True
            
        return False