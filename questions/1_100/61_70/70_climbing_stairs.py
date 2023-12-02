# coding=utf-8

class Solution:
    def climbStairs1(self, n: int) -> int:
        """
        会超时
        :param n:
        :return:
        """
        if n in (0, 1):
            return 1
        return self.climbStairs1(n - 1) + self.climbStairs1(n - 2)

    def climbStairs2(self, n: int) -> int:
        stairs_list = [0] * (n + 1)
        stairs_list[0] = 1
        stairs_list[1] = 1
        for i in range(2, n + 1):
            stairs_list[i] = stairs_list[i - 1] + stairs_list[i - 2]
        return stairs_list[-1]

    def climbStairs3(self, n: int) -> int:
        dp_1 = 0
        dp_2 = 0
        dp_3 = 1
        for i in range(n):
            dp_1 = dp_2
            dp_2 = dp_3
            dp_3 = dp_1 + dp_2
        return dp_3


class Solution2:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

    def climbStairs2(self, n: int) -> int:
        dp1, dp2, dp3 = 1, 1, 2
        if n == 1:
            return dp2
        for i in range(2, n):
            dp1, dp2, dp3 = dp2, dp3, dp2 + dp3
        return dp3


class Solution3:
    def climbStairs1(self, n: int) -> int:
        dp1, dp2, dp3 = 1, 1, 2
        if n == 1:
            return dp2
        for i in range(2, n):
            dp1, dp2, dp3 = dp2, dp3, dp2 + dp3
        return dp3



if __name__ == '__main__':
    n = 5
    s = Solution2()
    print(s.climbStairs(n))
