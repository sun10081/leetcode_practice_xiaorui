# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1598_crawler_log_folder.py
@time: 2022-09-09 23:53:38 
"""
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        for log in logs:
            if log == "./":
                continue
            elif log == "../" and ans > 0:
                ans -= 1
            elif log == "../":
                continue
            else:
                ans += 1
        return ans