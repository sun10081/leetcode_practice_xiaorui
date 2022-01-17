from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 边缘case
        s_len, p_len = len(s), len(p)
        if len(s) < len(p):
            return []
        # 初始化
        ans = []
        s_count = [0] * 26
        p_count = [0] * 26
        # 计数                                    字母出现次数
        for i in range(p_len):
            s_count[ord(s[i]) - ord('a')] += 1
            p_count[ord(p[i]) - ord('a')] += 1
        if s_count == p_count:
            ans.append(0)

        for i in range(p_len, s_len):
            s_count[ord(s[i - p_len]) - ord('a')] -= 1
            s_count[ord(s[i]) - ord('a')] += 1
            if s_count == p_count:
                ans.append(i - p_len + 1)
        return ans


if __name__ == '__main__':
    so = Solution()
    s = "abab"
    p = "ab"
    print(so.findAnagrams(s, p))
