# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2383_minimum_hours.py
@time: 2023-03-13 11:52:29 
"""
from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        sum_energy = sum(energy)
        ans = 0 if sum_energy < initialEnergy else 1 + sum_energy - initialEnergy
        cur_experience = initialExperience
        for exp in experience:
            if cur_experience <= exp:
                ans += 1 + exp - cur_experience
                cur_experience += 1 + exp - cur_experience
            cur_experience += exp
        return ans


if __name__ == '__main__':
    s = Solution()
    initialEnergy = 5
    initialExperience = 3
    energy = [1, 4]
    experience = [2, 5]
    print(s.minNumberOfHours(initialEnergy, initialExperience, energy, experience))

