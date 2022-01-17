# coding=utf-8


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == len(name)


if __name__ == '__main__':
    res = Solution()
    name = 'laiden'
    typed = 'laiden'
    print(res.isLongPressedName(name=name, typed=typed))
