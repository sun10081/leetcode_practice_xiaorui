# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 722_remove_comments.py
@time: 2023-08-08 01:32:14 
"""
from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        cur_line = []
        is_block = False

        for line in source:
            n = len(line)
            i = 0
            while i < n:
                if is_block:
                    if i + 1 < n and line[i] == '*' and line[i + 1] == '/':
                        is_block = False
                        i += 1
                else:
                    if i + 1 < n and line[i] == '/' and line[i + 1] == '*':
                        is_block = True
                        i += 1
                    elif i + 1 < n and line[i] == '/' and line[i + 1] == '/':
                        break
                    else:
                        cur_line.append(line[i])
                i += 1
            if not is_block and len(cur_line) > 0:
                ans.append("".join(cur_line))
                cur_line.clear()
        return ans


class Solution1:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        in_comment = False
        cur_line = []

        for line in source:
            i = 0
            n = len(line)
            while i < n:
                if in_comment:
                    if line[i] == '*' and i + 1 < n and line[i + 1] == '/':
                        in_comment = False
                        i += 1
                else:
                    if line[i] == '/' and i + 1 < n and line[i + 1] == '*':
                        in_comment = True
                        i += 1
                    elif line[i] == '/' and i + 1 < n and line[i + 1] == '/':
                        break
                    else:
                        cur_line.append(line[i])
                i += 1

            if not in_comment and len(cur_line) > 0:
                ans.append("".join(cur_line))
                cur_line.clear()
        return ans


class Solution2:
    def removeComments(self, source: List[str]) -> List[str]:
        ans = []
        cur_line = []
        in_comment = False

        for line in source:
            n = len(line)
            i = 0
            while i < n:
                if in_comment:
                    if line[i] == '*' and i + 1 < n and line[i + 1] == '/':
                        in_comment = False
                        i += 1
                else:
                    if line[i] == '/' and i + 1 < n and line[i + 1] == '/':
                        break
                    elif line[i] == '/' and i + 1 < n and line[i + 1] == '*':
                        in_comment = True
                        i += 1
                    else:
                        cur_line.append(line[i])
                i += 1
            if not in_comment and len(cur_line) > 0:
                ans.append("".join(cur_line))
                cur_line.clear()
        return ans


if __name__ == '__main__':
    s = Solution2()
    source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;",
              "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
    print(s.removeComments(source))
