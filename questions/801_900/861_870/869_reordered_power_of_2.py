# coding=utf-8

from typing import List


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        res = self.powerOf2Digits()
        n_counts = self.countDigits(n)
        for i in res:
            if n_counts == res[i]:
                return True
        return False

    def countDigits(self, n: int):
        cnt = [0] * 10
        while n:
            cnt[n % 10] = cnt[n % 10] + 1
            n = n // 10
        return tuple(cnt)

    def powerOf2Digits(self):
        res = {}
        for i in range(30):
            counts = self.countDigits(1 << i)
            res[i] = counts
        return res


if __name__ == '__main__':
    c = Solution()
    print(c.reorderedPowerOf2(3))
    # ans = {c.countDigits(1 << i) for i in range(30)}
    # print(ans)
