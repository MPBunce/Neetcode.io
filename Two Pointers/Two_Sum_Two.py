#Brute Force Time limit Solution 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        index = []

        for i in range( len(numbers) ):
            for j in range(i+1, len(numbers) ):
                res = numbers[i] + numbers[j]
                if res == target:
                    index.append(i+1)
                    index.append(j+1)
                    return index
                
#Accepted Solution 
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        left = 0
        right = len(numbers) - 1

        while left < right:
            curSum = numbers[left] + numbers[right]

            if curSum > target:
                right -= 1
            elif curSum < target:
                left += 1
            if curSum == target:
                return[left+1, right+1]      

        return []      