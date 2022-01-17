# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 9_palindrome_number
@time: 2022/1/13 11:42 下午
@desc: 
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        ans = []
        while x:
            ans.append(x % 10)
            x = x // 10
        return ans == ans[::-1]


if __name__ == '__main__':
    x = 1
    s = Solution()
    print(s.isPalindrome(x))
