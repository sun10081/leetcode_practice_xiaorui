# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 139_word_break
@time: 2021/12/29 11:46 下午
@desc: 
"""
from functools import lru_cache
from typing import List


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                node.children[index] = Trie()
            node = node.children[index]
        node.is_end = True

    @lru_cache(maxsize=128)
    def dfs(self, word: str, begin_index: int) -> bool:
        n = len(word)
        if begin_index == n:
            return True
        node = self
        for i in range(begin_index, n):
            index = ord(word[i]) - ord('a')
            node = node.children[index]
            if not node:
                return False
            if node.is_end and self.dfs(word, i + 1):
                return True
        return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = Trie()
        for word in wordDict:
            root.insert(word)
        return root.dfs(s, 0)


class Trie2:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str):
        node = self
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                node.children[index] = Trie2()
            node = node.children[index]
        node.is_end = True

    @lru_cache(maxsize=128)
    def dfs(self, word: str, begin_index) -> bool:
        node = self
        n = len(word)
        if begin_index == n:
            return True
        for i in range(begin_index, n):
            index = ord(word[i]) - ord('a')
            node = node.children[index]
            if not node:
                return False
            if node.is_end and self.dfs(word, i + 1):
                return True
        return False


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = Trie2()
        for word in wordDict:
            root.insert(word)
        return root.dfs(s, 0)


if __name__ == '__main__':
    solu = Solution2()
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(solu.wordBreak(s, wordDict))
