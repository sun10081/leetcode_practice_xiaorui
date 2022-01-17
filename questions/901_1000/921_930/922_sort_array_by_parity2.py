# coding=utf-8

from typing import List


class Solution:
    # def sortArrayByParity(self, A: List[int]) -> List[int]:
    #     return ([x for x in A if x % 2 == 0] + [x for x in A if x % 2 == 1])

    def sortArrayByParity2(self, A: List[int]) -> List[int]:
        i, j = 0, 1
        while i < len(A):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
            i += 2
        return A


if __name__ == '__main__':
    res = Solution()
    array = [4, 2, 5, 7]
    print(res.sortArrayByParity2(array))

