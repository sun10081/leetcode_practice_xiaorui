# coding=utf-8

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        mid = (1 + n) // 2
        while 1 <= mid <= n:
            res = self.guess(mid)
            if res == 0:
                return mid
            elif res > 0:
                left = mid
                mid = (right + left) // 2 + 1
            else:
                right = mid
                mid = (right + left) // 2
        return 0

    def guess(self, n: int) -> int:
        a = 6
        if n == a:
            return 0
        if n > a:
            return -1
        return 1


if __name__ == '__main__':
    s = Solution()
    n = 10
    print(s.guessNumber(n))
