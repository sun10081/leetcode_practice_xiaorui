# coding=utf-8

from typing import List
from collections import defaultdict, Counter


class Solution:
    def find_lhs1(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        max_len = 0
        for key, value in counts.items():
            if (key + 1) in counts:
                max_len = max(max_len, counts[key] + counts[key + 1])
        return max_len

    def find_lhs2(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return max((value + counts[key + 1] for key, value in counts.items() if key + 1 in counts), default=0)


if __name__ == '__main__':
    nums = [1, 1, 1, 1]
    nums.pop()
    s = Solution()
    print(s.find_lhs2(nums))
