# 1480. Running Sum of 1d Array
# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]

        for i in range(len(nums)):
            if i > 0:
                new_sum = result[i - 1] + nums[i]
                result.append(new_sum)
        return result
