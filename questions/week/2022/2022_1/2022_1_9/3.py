# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 3
@time: 2022/1/9 10:29 上午
@desc: 
"""
from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        ans = 0
        # res = []
        for target_word in targetWords:
            target_arr = list(target_word)
            target_arr.sort()
            for start_word in startWords:
                if len(target_arr) - len(start_word) == 1 and self.check_str(target_arr, start_word):
                    tmp_ch = self.find_ch(target_arr, start_word)
                    if tmp_ch not in start_word:
                        ans += 1
                        # res.append((start_word, target_word))
                        break
        return ans

    def check_str(self, target, word):
        for ch in word:
            if ch not in target:
                return False
        return True

    def find_ch(self, target, word):
        for ch in target:
            if ch not in word:
                return ch
        return ""


class Solution2:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        ans = 0
        # 对startWords进行排序重排
        start_words = set(''.join(sorted(w)) for w in startWords)
        # 遍历targetWords
        for target_word in targetWords:
            # 排序重排
            target = ''.join(sorted(target_word))
            # 去除target的每个元素，看是否能和start_words中单词匹配
            for i in range(len(target)):
                if target[:i] + target[i + 1:] in start_words:
                    ans += 1
                    break
        return ans

    def wordCount2(self, startWords: List[str], targetWords: List[str]) -> int:
        ans = 0
        # 对startWords进行排序重排
        start_words = set(''.join(sorted(w)) for w in startWords)
        # 遍历targetWords
        for target_word in targetWords:
            # 排序重排
            target = ''.join(sorted(target_word))
            # 去除target的每个元素，看是否能和start_words中单词匹配
            ans += any(target[:i] + target[i + 1:] in start_words for i in range(len(target)))
        return ans


if __name__ == '__main__':
    startWords = ["ant", "act", "tack"]
    targetWords = ["tack", "act", "acti"]
    s = Solution2()
    print(s.wordCount(startWords, targetWords))
