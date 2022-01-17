# coding=utf-8

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            if len(set(s)) < len(goal):
                return True
            return False
        diff = [(a, b) for a, b in zip(s, goal) if a != b]
        return len(diff) == 2 and diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]


if __name__ == '__main__':
    s = "ab"
    goal = "babbb"
    so = Solution()
    print(so.buddyStrings(s, goal))