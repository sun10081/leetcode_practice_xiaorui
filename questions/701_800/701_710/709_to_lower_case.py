# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 709_to_lower_case
@time: 2021/12/12 9:16 上午
@desc: 
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()

    def toLowerCase2(self, s: str) -> str:
        return "".join([chr(ord(ch) | 32) if 65 <= ord(ch) <= 90 else ch for ch in s])

    def toLowerCase3(self, s: str) -> str:
        # 大写字母的ascii码范围在[65, 90]，小写字母在[97, 122]，相差32
        # [65, 90]在二进制的表示为[01000001, 01011010], 32的二进制为00100000
        # 所以只需要大写字母的ascii码与32做与操作 即可得到小写字母
        s_array = []
        for ch in s:
            if 65 <= ord(ch) <= 90:
                ch = chr(ord(ch) | 32)
            s_array.append(ch)
        return "".join(s_array)


if __name__ == '__main__':
    s = "LOVELY"
    so = Solution()
    print(so.toLowerCase3(s))

