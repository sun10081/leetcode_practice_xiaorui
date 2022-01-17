from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        if s == t:
            return 0

        s_len = len(s)
        s_counts = [0] * 26
        t_counts = [0] * 26
        for i in range(s_len):
            s_counts[ord(s[i]) - 97] += 1
            t_counts[ord(t[i]) - 97] += 1

        # s_counts [1,2 ...]
        # t_counts [2,1 ...]

        ans = 0
        while s_counts != t_counts:
            p_left, p_right = 0, 0
            for i in range(26):
                if s_counts[i] > t_counts[i]:
                    p_left = i
                    continue
                if s_counts[i] < t_counts[i]:
                    p_right = i
                    continue
                if p_left and p_right:
                    break

            s_counts[p_left] -= 1
            s_counts[p_right] += 1

            ans += 1
        return ans

    def minSteps2(self, s: str, t: str) -> int:
        if s == t:
            return 0

        s_len = len(s)
        s_counts = [0] * 26
        t_counts = [0] * 26
        for i in range(s_len):
            s_counts[ord(s[i]) - 97] += 1
            t_counts[ord(t[i]) - 97] += 1

        # s_counts [1,2 ...]
        # t_counts [2,1 ...]

        ans = 0
        for i in range(26):
            if s_counts[i] < t_counts[i]:
                ans += t_counts[i] - s_counts[i]
        return ans


if __name__ == '__main__':
    s = "friend"
    t = "family"
    # print(Counter(s))
    so = Solution()
    print(so.minSteps2(s, t))
