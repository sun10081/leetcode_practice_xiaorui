# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 913_cat_and_mouse
@time: 2022/1/4 10:22 上午
@desc: 
"""
from typing import List

DRAW = 0
MOUSE_WIN = 1
CAT_WIN = 2


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:

        def get_result(mouse: int, cat: int, turns: int) -> int:
            if turns == 2 * n:
                return DRAW
            res = dp[mouse][cat][turns]
            if res != -1:
                return res
            if mouse == 0:
                res = MOUSE_WIN
            elif cat == mouse:
                res = CAT_WIN
            else:
                res = get_next_result(mouse, cat, turns)
            dp[mouse][cat][turns] = res
            return res

        def get_next_result(mouse: int, cat: int, turns: int) -> int:
            cur_move = mouse if turns % 2 == 0 else cat
            default_res = MOUSE_WIN if cur_move != mouse else CAT_WIN
            res = default_res
            for next_move in graph[cur_move]:
                if cur_move == cat and next_move == 0:
                    continue
                next_mouse = next_move if cur_move == mouse else mouse
                next_cat = next_move if cur_move == cat else cat
                next_res = get_result(next_mouse, next_cat, turns + 1)
                if next_res != default_res:
                    res = next_res
                    if res != DRAW:
                        break
            return res

        n = len(graph)
        dp = [[[-1] * (n * 2) for _ in range(n)] for _ in range(n)]
        return get_result(1, 2, 0)
