# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 472_concatenated_words
@time: 2021/12/28 10:11 上午
@desc: 
"""
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

    def dfs(self, word: str, begin_index: int) -> bool:
        if begin_index == len(word):
            return True
        node = self
        for i in range(begin_index, len(word)):
            index = ord(word[i]) - ord('a')
            node = node.children[index]
            if node is None:
                return False
            if node.is_end and self.dfs(word, i + 1):
                return True
        return False


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        # words.sort(key=lambda x: len(x))
        ans = []
        root = Trie()
        for word in words:
            if word == "":
                continue
            if root.dfs(word, 0):
                ans.append(word)
            else:
                root.insert(word)
        return ans


class Trie2:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                node.children[index] = Trie2()
            node = node.children[index]
        node.is_end = True

    def dfs(self, word: str, begin_index: int) -> bool:
        n = len(word)
        if begin_index == n:
            return True

        node = self
        for i in range(begin_index, n):
            index = ord(word[i]) - ord('a')
            node = node.children[index]
            if node is None:
                return False
            elif node.is_end and self.dfs(word, i + 1):
                return True
        return False


class Solution2:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []
        words.sort(key=len)
        root = Trie2()
        for word in words:
            if word == "":
                continue
            if root.dfs(word, 0):
                ans.append(word)
            else:
                root.insert(word)
        return ans



if __name__ == '__main__':
    words = ["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]
    s = Solution2()
    print(s.findAllConcatenatedWordsInADict(words))

