# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2325_decode_the_message.py
@time: 2023-02-01 09:11:10 
"""
from collections import defaultdict


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_map = defaultdict()
        index = 0
        for ch in key:
            if index > 25:
                break

            if ch in key_map or ch == " ":
                continue
            key_map[ch] = chr(ord('a') + index)
            index += 1

        ans = []
        for ch in message:
            if ch == " ":
                ans.append(ch)
            else:
                ans.append(key_map[ch])

        return "".join(ans)


if __name__ == '__main__':
    key = "the quick brown fox jumps over the lazy dog"
    message = "vkbs bs t suepuv"
    s = Solution()
    print(s.decodeMessage(key, message))
