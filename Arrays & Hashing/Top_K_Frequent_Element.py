#Fancy Sorting

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for n in nums:
            if n in res:
                res[n] += 1
            else:
                res[n] = 1
        
        res_list = []
        # Sort the dictionary by values in descending order
        sorted_res = sorted(res.items(), key=lambda x: x[1], reverse=True)

        # Extract the top K frequent elements
        top_k_elements = [key for key, value in sorted_res[:k]]

        return top_k_elements
    
#Manual Soultion w worse runtime
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for n in nums:
            if n in res:
                res[n] += 1
            else:
                res[n] = 1
        
        res_list = []

        for i in range(k):
            temp = 0
            t_key = 0
            for key in res:

                if key not in res_list and res[key] > temp:
                    temp = res[key]
                    t_key = key
                
            res_list.append(t_key)
            
        return res_list
        
