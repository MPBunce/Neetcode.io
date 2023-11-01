class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for input_strs in strs:
            sorted_str = str( sorted(input_strs) )
            print(sorted_str, input_strs)
            if sorted_str in res:
                res[sorted_str].append( input_strs ) 
            else:
                res[sorted_str] = [ input_strs ]

        return res.values()