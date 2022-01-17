# coding=utf-8


from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        kinds_of_candy = len(set(candyType))
        half_count_of_candy = len(candyType) // 2
        return min(kinds_of_candy, half_count_of_candy)


if __name__ == '__main__':
    candyType = [1, 1, 2, 2, 3, 3]
    s = Solution()
    print(s.distributeCandies(candyType))
