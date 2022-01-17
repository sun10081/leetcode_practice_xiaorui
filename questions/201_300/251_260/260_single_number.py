# coding=utf-8

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor_sum = 0
        for num in nums:
            xor_sum = xor_sum ^ num

        low_index = 1
        while xor_sum & low_index == 0:
            low_index = low_index << 1
        list1 = list2 = 0
        for num in nums:
            if low_index & num == 0:
                list1 = list1 ^ num
            else:
                list2 = list2 ^ num
        return [list1, list2]


if __name__ == '__main__':
    pass
