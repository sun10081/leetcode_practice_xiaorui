# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: letter-combinations
@time: 2023/6/26 12:08 PM
@desc:
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(index):
            if index == len(digits):
                combinations.append("".join(combination))
            else:
                digit = digits[index]
                for letter in phone_map[digit]:
                    combination.append(letter)
                    backtrack(index + 1)
                    combination.pop()

        combination = []
        combinations = []
        backtrack(0)
        return combinations


class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i):
            if i == n:
                ans.append("".join(path))
                return
            if i > n:
                return
            for ch in phone_map[digits[i]]:
                path.append(ch)
                dfs(i + 1)
                path.pop()

        ans = []
        path = []
        n = len(digits)
        dfs(0)
        return ans


if __name__ == '__main__':
    s = Solution2()
    digits = "23"
    print(s.letterCombinations(digits))
