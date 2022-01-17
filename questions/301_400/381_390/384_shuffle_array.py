# coding=utf-8


from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.reset_array = nums.copy()

    def reset(self) -> List[int]:
        return self.reset_array

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums)
        return self.nums

    def shuffle1(self) -> List[int]:
        l = len(self.nums)
        for i in range(l):
            j = random.randrange(i, l)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


if __name__ == '__main__':
    nums = [1, 3, 2]
    s = Solution(nums)
    print(s.shuffle1())
    print(s.reset())
