# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1333_filter_restaurants.py
@time: 2023-09-27 17:05:32 
"""
from typing import List


class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        filtered = []
        for restaurant in restaurants:
            if ((veganFriendly and restaurant[2]) or not veganFriendly) and restaurant[3] <= maxPrice and restaurant[4] <= maxDistance:
                filtered.append(restaurant)
        filtered.sort(key=lambda x: (-x[1], -x[0]))
        return list(f[0] for f in filtered)
