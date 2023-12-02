# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1817_finding_the_users_active_minutes.py
@time: 2023-01-20 08:55:00 
"""
from typing import List
from collections import defaultdict


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        count = defaultdict(int)
        for log in logs:
            for id, minute in log:

