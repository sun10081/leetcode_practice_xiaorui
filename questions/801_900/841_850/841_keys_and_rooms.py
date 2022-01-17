# coding=utf-8

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(s: str) -> str:
            l = list()
            for item in s:
                if item != '#':
                    l.append(item)
                elif l:
                    l.pop()
            return ''.join(l)

        return build(S) == build(T)


if __name__ == '__main__':
    s = Solution()
    S = "a#c"
    T = "b"
    print(s.backspaceCompare(S, T))
