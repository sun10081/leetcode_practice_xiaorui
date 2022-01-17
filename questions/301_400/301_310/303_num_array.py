# coding=utf-8

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        _sums = self.sums

        for num in nums:
            _sums.append(_sums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        _sums = self.sums
        return _sums[j + 1] - _sums[i]


if __name__ == '__main__':
    array = [-2, 0, 3, -5, 2, -1]
    i = 0
    j = 2
    c = NumArray(array)
    print(c.sumRange(i, j))


