from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
        trust_count = [0] * (n + 1)
        # 被人信任 数量+1 信任别人 数量-1
        for couple_people in trust:
            trust_count[couple_people[0]] -= 1
            trust_count[couple_people[1]] += 1
        for i in range(1, n + 1):
            if trust_count[i] == n - 1:
                return i
        return -1


if __name__ == '__main__':
    n = 1
    trust = []
    s = Solution()
    print(s.findJudge(n, trust))
