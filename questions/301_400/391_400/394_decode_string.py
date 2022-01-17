# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 394_decode_string
@time: 2021/12/4 9:35 下午
@desc: 
"""

class Solution:
    def decodeString(self, s: str) -> str:
        """
        本题核心思路是在栈里面每次存储两个信息, (左括号前的字符串, 左括号前的数字), 比如abc3[def],
        当遇到第一个左括号的时候，压入栈中的是("abc", 3), 然后遍历括号里面的字符串def,
        当遇到右括号的时候, 从栈里面弹出一个元素(s1, n1), 得到新的字符串为s1+n1*"def", 也就是abcdefdefdef。对于括号里面嵌套的情况也是同样处理方式。
        凡是遇到左括号就进行压栈处理，遇到右括号就弹出栈，栈中记录的元素很重要。
        """
        stack = []
        res = ""
        num = 0
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append((res, num))
                num = 0
                res = ""
            elif ch == "]":
                top = stack.pop()
                res = top[0] + res * top[1]
            else:
                res += ch
        return res


class Solution2:
    def decodeString(self, s: str) -> str:
        ans = ""
        num = 0
        stack = []
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((ans, num))
                num = 0
                ans = ""
            elif ch == "]":
                top = stack.pop()
                ans = top[0] + ans * top[1]
            else:
                ans += ch
        return ans


class Solution3:
    def decodeString(self, s: str) -> str:
        num = 0
        ans = ""
        stack = []
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack.append((ans, num))
                ans = ''
                num = 0
            elif ch == ']':
                top = stack.pop()
                ans = top[0] + ans * top[1]
            else:
                ans += ch
        return ans


if __name__ == '__main__':
    s = "3[a2[c]]"
    # accaccacc
    so = Solution3()
    print(so.decodeString(s))



