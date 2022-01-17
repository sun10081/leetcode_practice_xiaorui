# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 71_simplify_path
@time: 2022/1/6 10:21 上午
@desc: 
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        path_arr = path.split("/")
        stack = []
        for single_path in path_arr:
            if stack and single_path == "..":
                stack.pop()
            elif single_path and single_path not in [".", ".."]:
                stack.append(single_path)
        return "/" + "/".join(stack)


if __name__ == '__main__':
    s = Solution()
    path = "/../"
    print(s.simplifyPath(path))
