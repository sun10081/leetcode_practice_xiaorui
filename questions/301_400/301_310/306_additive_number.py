# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 306_additive_number.py
@time: 2022-01-10 10:30:20 
"""


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        return self.dfs(num, 0, 0, 0, 0)

    def dfs(self, num: str, index: int, count: int, first: int, second: int) -> bool:
        n = len(num)
        if index >= n:
            # count代表当前有效数字的数量，遍历结束未返回false且数量大于2，即为累加数
            return count > 2
        cur = 0
        for i in range(index, n):
            # 剪枝1 忽略前导0的情况
            if num[index] == '0' and i > index:
                return False

            ch = num[i]
            cur = cur * 10 + int(ch)
            if count >= 2:
                third = first + second
                # 剪枝2 大于前两数之和
                if cur > third:
                    return False
                # 剪枝3 继续添加数字
                elif cur < third:
                    continue

            if self.dfs(num, i + 1, count + 1, second, cur):
                return True

        return False


class Solution2:
    def isAdditiveNumber(self, num: str) -> bool:
        return self.dfs(num, 0, 0, 0, 0)

    def dfs(self, num: str, index: int, count: int, first: int, second: int) -> bool:
        n = len(num)
        if index >= n:
            return count > 2
        if len(str(first)) > 17 or len(str(second)) > 17:
            return False
        cur = 0
        for i in range(index, n):
            if num[index] == '0' and i > index:
                return False
            cur = 10 * cur + int(num[i])
            if count >= 2:
                third = first + second
                if cur > third:
                    return False
                elif cur < third:
                    continue
            if self.dfs(num, i + 1, count + 1, second, cur):
                return True
        return False


if __name__ == '__main__':
    num = "1023"
    s = Solution2()
    print(s.isAdditiveNumber(num))
