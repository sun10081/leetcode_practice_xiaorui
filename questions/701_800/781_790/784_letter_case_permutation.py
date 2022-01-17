# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 784_letter_case_permutation
@time: 2021/12/22 2:51 下午
@desc: 
"""
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def dfs(begin_index: int) -> None:
            if begin_index == n:
                ans.append("".join(sequence[:]))
                return

            if s[begin_index].isdigit():
                sequence.append(s[begin_index])
                dfs(begin_index + 1)
                sequence.pop()

            elif s[begin_index].islower():
                sequence.append(s[begin_index])
                dfs(begin_index + 1)
                sequence.pop()
                sequence.append(s[begin_index].upper())
                dfs(begin_index + 1)
                sequence.pop()

            # elif s[begin_index].isupper():
            #     sequence.append(s[begin_index])
            #     dfs(begin_index + 1)
            #     sequence.pop()
            #     sequence.append(s[begin_index].lower())
            #     dfs(begin_index + 1)
            #     sequence.pop()

        n = len(s)
        ans = []
        sequence = []
        dfs(0)
        return ans


if __name__ == '__main__':
    S = "3z4"
    s = Solution()
    print(s.letterCasePermutation(S))
