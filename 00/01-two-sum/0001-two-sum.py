from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}                             # 1

        for index, num in enumerate(nums):   # 2
            if num in map:                   # 3
                return [map[num], index]
            else:
                map[target-num] = index      # 4


"""
complement = target - nums[index]

1. initialize map to store seen key(target's complement) and value(index of other complement)

2. get index of current iteration and num value/item at current iteration,
    by looping through iterable object nums with enumerate(nums)
    

3. if current num complement already exists in map, we found a solution,
    return the indices of the complement nums

4. add to map - complement key paired with value (index of other complement)

"""
# Input: nums=[2, 7, 11, 15], target=9
# _______________________________________
# step#4       index: 0       num: 2
#
#         [2, 7, 11, 15]      map = {}
#          ^
#      9 - 2 = 7 (complement)
# target - num
#
# map[complement] = index
#             map = {7:0}
# _______________________________________
# step#3       index: 1       num: 7
#
#       [2, 7, 11, 15]         map = {7:0}
#           ^
#       9 - 7 = 2 (complement)
#  target - num
#
# return [map[num], index]
#                ^  ^
# Ouput:        [0, 1]
# _______________________________________

assert(Solution().twoSum(nums=[2, 7, 11, 15], target=9) == [0, 1])
assert(Solution().twoSum(nums=[3, 2, 4], target=6) == [1, 2])
assert(Solution().twoSum(nums=[3, 3], target=6) == [0, 1])


def main():

    output = Solution().twoSum(nums=[2, 7, 11, 15], target=9)
    print(f"Output: {output}")


if __name__ == '__main__':
    main()
