#Brute force O(n^2)
#Time Limit Exceeded
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range( len(temperatures) ):
            count = 1
            for j in range( i+1, len(temperatures) ):
                if temperatures[i] < temperatures[j]:
                    res.append(count)
                    break
                elif j == len(temperatures)-1:
                    res.append(0)
                else:
                    count += 1

        res.append(0)
         
        return res
    

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res