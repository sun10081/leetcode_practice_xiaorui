# coding=utf-8

from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        length = len(A)
        for item in range(length - 1, 1, -1):
            if A[item - 1] + A[item - 2] > A[item]:
                return A[item] + A[item - 1] + A[item - 2]
        return 0


if __name__ == '__main__':
    c = Solution()
    a = [3,2,3,4]
    print(c.largestPerimeter(a))

