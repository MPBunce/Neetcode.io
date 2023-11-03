class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sorted_num = sorted(nums)
        count = 1
        max = 1

        if len(nums) < 1:
            return 0

        for i in range( len(sorted_num)-1 ):

            if sorted_num[i] + 1 == sorted_num[i+1]:
                count += 1
            elif sorted_num[i] == sorted_num[i+1]:
                pass
            else:
                print(count, max)
                if count > max:
                    max = count

                count = 1


        if count > max:
            max = count


        return max