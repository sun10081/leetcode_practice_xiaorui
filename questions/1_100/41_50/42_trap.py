# coding=utf-8

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        nums = len(height)
        left_max_array = [height[0]] + [0] * (nums - 1)
        for i in range(1, nums):
            left_max_array[i] = max(left_max_array[i - 1], height[i])

        right_max_array = [0] * (nums - 1) + [height[nums - 1]]
        for i in range(nums - 2, -1, -1):
            right_max_array[i] = max(height[i], right_max_array[i + 1])

        total_array = [0] * nums
        for i in range(nums):
            total_array[i] = min(left_max_array[i], right_max_array[i]) - height[i]
        return sum(total_array)


if __name__ == '__main__':
    height = [4,2,0,3,2,5]
    s = Solution()
    print(s.trap(height))
