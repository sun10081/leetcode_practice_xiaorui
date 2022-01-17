from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        直接排序
        :param s:
        :param t:
        :return:
        """
        if s == t:
            return True
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        """
        哈希表
        :param s:
        :param t:
        :return:
        """
        if len(s) != len(t):
            return False
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        for c in t:
            counts[c] = counts.get(c, 0) - 1
        for value in counts.values():
            if value != 0:
                return False
        return True

    def isAnagram3(self, s: str, t: str) -> bool:
        """
        数组
        :param s:
        :param t:
        :return:
        """
        if len(s) != len(t):
            return False
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        for c in t:
            counts[ord(c) - ord('a')] -= 1
            if counts[ord(c) - ord('a')] < 0:
                return False
        return True


if __name__ == '__main__':
    s = "car"
    t = "rat"
    so = Solution()
    print(so.isAnagram3(s, t))