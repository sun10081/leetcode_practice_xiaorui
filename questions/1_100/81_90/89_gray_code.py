# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 721_gray_code
@time: 2022/1/8 10:36 上午
@desc: 
"""
from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n + 1):
            cur_len = len(ans)
            # 倒着+1，才能确保相邻数只有一位不同
            for j in range(cur_len - 1, -1, -1):
                ans.append(ans[j] | 1 << (i - 1))
        return ans

    def grayCode2(self, n: int) -> List[int]:
        ans = []
        for i in range(1 << n):
            ans.append(i ^ (i >> 1))
        return ans


class Solution2:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n + 1):
            cur_len = len(ans)
            for j in range(cur_len - 1, -1, -1):
                ans.append(ans[j] | 1 << (i - 1))
        return ans


if __name__ == '__main__':
    n = 3
    s = Solution2()
    print(s.grayCode(n))
