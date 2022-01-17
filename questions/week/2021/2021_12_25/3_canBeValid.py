# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 3_canBeValid
@time: 2021/12/25 10:59 下午
@desc: 
"""


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if self.isValid(s):
            return True
        left_count, right_count = 0, 0
        s_arr = list(s)
        for i in range(len(s)):
            if s_arr[i] == "(":
                left_count += 1
            else:
                right_count += 1
            if right_count > left_count:
                if locked[i] == "0" and s_arr[i] == ")":
                    s_arr[i] = "("
                    left_count += 1
                    right_count -= 1
            elif left_count > right_count:
                if locked[i] == "0" and s_arr[i] == "(":
                    s_arr[i] = ")"
                    left_count -= 1
                    right_count += 1
        s_tmp = "".join(s_arr)
        if self.isValid(s_tmp):
            return True

        # left_count, right_count = 0, 0
        # s_arr = list(s)

        # for i in range(len(s) - 1, -1, -1):
        #     if s_arr[i] == "(":
        #         left_count += 1
        #     else:
        #         right_count += 1
        #     if left_count > right_count:
        #         if locked[i] == "0" and s_arr[i] == "(":
        #             s_arr[i] = ")"
        #             left_count -= 1
        #             right_count += 1
        # s_tmp = "".join(s_arr)
        # if self.isValid(s_tmp):
        #     return True

        return False

    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        stack = []
        for ch in s:
            if ch == "(":
                stack.append(ch)
            else:
                if not stack:
                    return False
                tmp_ch = stack.pop()
                if (tmp_ch + ch) != "()":
                    return False
        return len(stack) == 0


class Solution2:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2:
            return False
        # 统计左右括号中不能改变的个数
        left_count, right_count = 0, 0
        for i in range(n):
            # 从左往右遍历，统计不能改变的右括号的个数
            if s[i] == ")" and locked[i] == "1":
                right_count += 1
            # 左括号的最大数量i + 1 - right_count ，坐标统计,从0开始算 所以计算个数要+1
            if i + 1 - right_count < right_count:
                return False

        for i in range(n - 1, -1, -1):
            # 从右往左遍历，统计不能改变的左括号的个数
            if s[i] == "(" and locked[i] == "1":
                left_count += 1
            # 右括号的最大数量n - 1 - i ，倒序遍历的 所以计算个数不需要+1
            if n - i - left_count < left_count:
                return False

        return True


if __name__ == '__main__':
    solu = Solution2()
    s = "))()))"
    locked = "010100"
    print(solu.canBeValid(s, locked))
    # print(l)
