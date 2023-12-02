# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 1233_remove_sub_folders_from_the_filesystem.py
@time: 2023-02-08 10:41:26 
"""
from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        ans = []
        pre = "123"
        for file in sorted(folder):
            if not file.startswith(pre):
                ans.append(file)
                pre = file + "/"
        return ans


if __name__ == '__main__':
    folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    s = Solution()
    print(s.removeSubfolders(folder))