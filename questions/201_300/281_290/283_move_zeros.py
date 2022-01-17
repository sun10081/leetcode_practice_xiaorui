# coding=utf-8

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = right = 0
        length = len(nums)
        while right < length:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


class Solution2:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left, right = 0, 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


class Solution3:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left, right = 0, 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


if __name__ == '__main__':
    nums = [1, 0, 1]
    s = Solution3()
    s.moveZeroes(nums)
    print(nums)
