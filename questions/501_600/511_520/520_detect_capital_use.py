# coding=utf-8

import re


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # 全部是大写
        pattern1 = r'^[A-Z]+$'
        if re.match(pattern1, word):
            return True

        # 全小写
        pattern2 = r'^[a-z]+$'
        if re.match(pattern2, word):
            return True

        # 首字母大写
        pattern3 = r'^[A-Z][a-z]+$'
        if re.match(pattern3, word):
            return True

        return False


if __name__ == '__main__':
    pattern1 = r'^[A-Z]+$'
    str1 = "USAa"
    # print(re.match(pattern1, str))
