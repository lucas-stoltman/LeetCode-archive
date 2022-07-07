# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        nums_sum = sum(nums)
        left_sum = 0
        for i, x in enumerate(nums):
            if left_sum == (nums_sum - left_sum - x):
                return i
            left_sum += x
        return -1
