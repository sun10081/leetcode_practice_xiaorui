# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 383_ransom_note
@time: 2021/12/4 9:48 上午
@desc: 
"""
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        count = [0] * 26
        for s in magazine:
            count[ord(s) - 97] += 1
        for s in ransomNote:
            if count[ord(s) - 97] == 0:
                return False
            count[ord(s) - 97] -= 1
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        ans = Counter(ransomNote) - Counter(magazine)
        return not ans


if __name__ == '__main__':
    so = Solution()
    ransomNote = 'aa'
    magazine = 'aab'
    print(so.canConstruct2(ransomNote, magazine))
