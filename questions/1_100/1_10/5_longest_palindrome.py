# coding=utf-8

from typing import List, Tuple


class Solution1:

    # 方法一 动态规划
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        # 记录长度，起始index
        max_len = 1
        begin = 0
        # 初始化dp
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i

        return s[begin:begin + max_len]

    # 方法二 中心扩散
    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome2(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]


class Solution2:
    # 中心扩散
    def longestPalindrome1(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> Tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1


class Solution3:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> Tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1


class Solution4:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(str)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 >= end - start:
                start, end = left1, right1
            if right2 - left2 >= end - start:
                start, end = left2, right2
        return s[start:end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> Tuple[int, int]:
        while left >= 0 and right < len(str) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1


class Solution5:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = 0, 0
        for i in range(n):
            start1, end1 = self.expandAroundCenter(s, i, i)
            start2, end2 = self.expandAroundCenter(s, i, i + 1)
            if end1 - start1 > end - start:
                start, end = start1, end1
            if end2 - start2 > end - start:
                start, end = start2, end2
        return s[start:end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> Tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1


class Solution6:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = 0, 0
        for i in range(n):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)

            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2

        return s[start:end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> Tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1


class Solution7:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start, end = 0, 0
        for i in range(n):
            start1, end1 = self.expandAroundCenter(s, i, i)
            start2, end2 = self.expandAroundCenter(s, i, i + 1)

            if end1 - start1 > end - start:
                start, end = start1, end1
            if end2 - start2 > end - start:
                start, end = start2, end2
        return s[start:end + 1]

    def expandAroundCenter(self, s: str, left: int, right: int) -> Tuple[int, int]:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1


if __name__ == '__main__':
    s = "cbbd"
    so = Solution7()
    print(so.longestPalindrome(s))
