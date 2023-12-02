# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1773_count_items.py
@time: 2022-10-29 10:53:17 
"""
from typing import List


class Solution:

    def __init__(self):
        self.rule_index_dict = {
            "type": 0,
            "color": 1,
            "name": 2
        }

    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey not in self.rule_index_dict:
            raise RuntimeError(f"rule key值异常")

        count = 0
        index = self.rule_index_dict[ruleKey]
        for item in items:
            if item[index] == ruleValue:
                count += 1
        return count

