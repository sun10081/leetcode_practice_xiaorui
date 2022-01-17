# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 208_implement_trie_prefix_tree
@time: 2021/12/28 9:55 上午
@desc: 
"""
from typing import Optional

class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                return None
            node = node.children[index]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                node.children[index] = Trie()
            node = node.children[index]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None



class Trie2:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

    def search_prefix(self, prefix: str) -> "Trie2":
        node = self
        for ch in prefix:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                return None
            node = node.children[index]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.children[index]:
                node.children[index] = Trie2()
            node = node.children[index]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.search_prefix(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:
        return self.search_prefix(prefix) is not None


if __name__ == '__main__':
    trie = Trie2()
    trie.insert("apple")
    res = trie.search("apple")
    print(res)

