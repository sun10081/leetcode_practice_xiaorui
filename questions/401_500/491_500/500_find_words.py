# coding=utf-8

import re
from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        pattern_of_first_line = "^[qwertyuiop]*$"
        pattern_of_second_line = "^[asdfghjkl]*$"
        pattern_of_third_line = "^[zxcvbnm]*$"
        res = []

        for word in words:
            if re.match(pattern_of_first_line, word, re.I) or re.match(pattern_of_second_line, word, re.I) or re.match(pattern_of_third_line, word, re.I):
                res.append(word)
        return res


if __name__ == '__main__':
    # pattern = "^[asdfghjkl]*$"
    # string = "Hello"
    # print(re.match(pattern, string, re.I))
    # c = Solution()
    # words = ["Hello","Alaska","Dad","Peace"]
    # print(c.findWords(words))

    pattern = "允许.*获取应用列表?"
    string = '允许"今日头条头条极速版"获取应用列表?'
    print(re.match(pattern, string, re.I))
