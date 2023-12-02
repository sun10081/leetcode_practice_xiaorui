# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 676_implement_magic_dictionary.py
@time: 2022-07-11 12:53:16 
"""
from typing import List


class MagicDictionary:

    def __init__(self):
        self.words = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.words = dictionary

    def search(self, searchWord: str) -> bool:
        for word in self.words:
            if len(word) != len(searchWord):
                continue
            diff = 0
            for chx, chy in zip(word, searchWord):
                if chx != chy:
                    diff += 1
                if diff > 1:
                    break
            if diff == 1:
                return True

        return False


if __name__ == '__main__':
    a = "hello"
    b = "helll"
    print(list(zip(a, b)))