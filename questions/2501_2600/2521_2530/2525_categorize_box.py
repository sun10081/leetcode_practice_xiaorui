# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2525_categorize_box.py
@time: 2023-10-20 12:21:12 
"""


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = False
        if length * width * height >= 10 ** 9 or any([i >= 10 ** 4 for i in [length, width, height]]):
            bulky = True
        heavy = True if mass >= 100 else False

        if bulky and heavy:
            return "both"
        elif bulky:
            return "Bulky"
        elif heavy:
            return "Heavy"
        else:
            return "Neither"
