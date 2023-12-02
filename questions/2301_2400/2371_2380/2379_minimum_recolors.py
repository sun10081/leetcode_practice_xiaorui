# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2379_minimum_recolors.py
@time: 2023-03-09 11:01:55 
"""


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = 101
        white_cnt = 0
        for i, block in enumerate(blocks):
            if block == 'W':
                white_cnt += 1
            if i >= k and blocks[i - k] == 'W':
                white_cnt -= 1
            if i >= k - 1:
                ans = min(ans, white_cnt)
        return ans


if __name__ == '__main__':
    s = Solution()
    blocks = "WBWBBBW"
    k = 2
    print(s.minimumRecolors(blocks, k))
