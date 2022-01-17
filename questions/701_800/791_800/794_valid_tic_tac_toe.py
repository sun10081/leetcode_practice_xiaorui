# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 794_valid_tic_tac_toe
@time: 2021/12/9 10:35 上午
@desc: 
"""
from typing import List
from collections import Counter, defaultdict


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        """
        1. O的数量只能和X相等或者-1
        2. x获胜时， 数量是O的+1
        3. O获胜时， 数量和X相同
        :param board:
        :return:
        """
        o_count = sum(row.count('O') for row in board)
        x_count = sum(row.count('X') for row in board)
        return not ((o_count != x_count and o_count - x_count != -1) or (
                o_count != x_count and self.win(board, "O")) or (o_count != x_count - 1 and self.win(board, "X")))

    def win(self, board: List[str], p: str) -> bool:
        return any((board[i][0] == p and board[i][1] and board[i][2]) or
                   (board[0][i] == p and board[1][i] == p and board[2][i] == p) for i in range(3) or
                   (board[0][0] == p and board[1][1] == p and board[2][2] == p) or
                   (board[0][2] == p and board[1][1] == p and board[2][0] == p))


class Solution2():
    def win(self, board: List[str], p: str) -> bool:
        return any(board[i][0] == p and board[i][1] == p and board[i][2] == p or
                   board[0][i] == p and board[1][i] == p and board[2][i] == p for i in range(3)) or \
               board[0][0] == p and board[1][1] == p and board[2][2] == p or \
               board[0][2] == p and board[1][1] == p and board[2][0] == p

    def validTicTacToe(self, board: List[str]) -> bool:
        oCount = sum(row.count('O') for row in board)
        xCount = sum(row.count('X') for row in board)
        return not (oCount != xCount and oCount != xCount - 1 or
                    oCount != xCount and self.win(board, 'O') or
                    oCount != xCount - 1 and self.win(board, 'X'))


if __name__ == '__main__':
    board = ["XOX", "O O", "XOX"]
    s = Solution2()
    print(s.validTicTacToe(board))
