# coding=utf-8

from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        length_of_a = len(A)
        for l in A:
            left = 0
            right = length_of_a - 1
            length_of_a = len(A)
            while left < right:
                if l[left] == l[right]:
                    l[left] = l[left] ^ 1
                    l[right] = l[right] ^ 1
                left += 1
                right -= 1
            if left == right:
                l[left] = l[left] ^ 1
        return A


if __name__ == '__main__':
    l = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    img = Solution()
    print(img.flipAndInvertImage(l))
