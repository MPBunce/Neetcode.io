def binary_search(nums: list[int], target: int) -> int:

    l = 0
    r = len(nums)-1
    
    while l <= r:
        m = (l + r) // 2
        if nums[m] > target:
            r = m-1
        elif nums[m] < target:
            l = m+1
        else: 
            return nums[m]

    return -1

def main():
    case_1 = [-1,0,3,5,9,12]
    t_1 = 9
    print(binary_search(case_1, t_1))

    case_2 = [-1,0,3,5,9,12]
    t_2 = 2
    print(binary_search(case_2, t_2))

main()