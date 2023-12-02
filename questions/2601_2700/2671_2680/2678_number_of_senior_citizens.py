# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2678_number_of_senior_citizens.py
@time: 2023-10-23 11:21:58 
"""
from typing import List


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans = 0
        for d in details:
            if int(d[-4:-2]) > 60:
                ans += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
    print(s.countSeniors(details))
