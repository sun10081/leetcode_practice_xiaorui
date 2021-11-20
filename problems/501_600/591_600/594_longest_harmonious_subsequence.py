from typing import List
from collections import defaultdict


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
        max_len = 0
        for key, value in counts.items():
            if (key + 1) in counts:
                max_len = max(max_len, counts[key] + counts[key + 1])
        return max_len


if __name__ == '__main__':
    nums = [1, 1, 1, 1]
    s = Solution()
    print(s.findLHS(nums))
