# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1410_html_entity_parser.py
@time: 2023-11-23 11:33:03 
"""
from typing import List


class Solution:

    def entityParser(self, text: str) -> str:
        entity_map = {
            '&quot;': '"',
            '&apos;': "'",
            '&gt;': '>',
            '&lt;': '<',
            '&frasl;': '/',
            '&amp;': '&',
        }

        i = 0
        n = len(text)
        ans = []
        while i < n:
            is_entity = False
            if text[i] == '&':
                for k, v in entity_map.items():
                    if text[i:i + len(k)] == k:
                        ans.append(v)
                        i += len(k)
                        is_entity = True
                        break
            if not is_entity:
                ans.append(text[i])
                i += 1
        return "".join(ans)


if __name__ == '__main__':
    s = Solution()
    text = "and I quote: &quot;...&quot;"
    print(s.entityParser(text))