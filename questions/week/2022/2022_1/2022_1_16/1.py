# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1
@time: 2022/1/16 10:31 上午
@desc: 
"""
from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        n = len(s)
        index = 0
        for i in range(n // k):
            ans.append(s[index:index+k])
            index += k
        if n % k == 0:
            return ans
        else:
            last_index = len(ans) * k - 1
            ans.append(s[last_index+1:])
            ans[-1] += (k - len(ans[-1])) * fill
        return ans


if __name__ == '__main__':
    s = "abcdefghi"
    k = 3
    fill = "x"
    sol = Solution()
    print(sol.divideString(s,k,fill))
