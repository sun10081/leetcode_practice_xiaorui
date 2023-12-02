from typing import List
from collections import defaultdict


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        """
        超时写法
        :param strs:
        :return:
        """

        def is_anagrams(s: str, t: str) -> bool:
            if s == t:
                return True
            return sorted(s) == sorted(t)

        res = []
        if len(strs) == 1:
            res.append(strs)
            return res

        level = []
        used = [False] * len(strs)
        for i in range(len(strs)):
            if used[i]:
                continue
            level.append(strs[i])
            used[i] = True
            for j in range(i + 1, len(strs)):
                if used[j]:
                    continue
                if is_anagrams(strs[i], strs[j]):
                    level.append(strs[j])
                    used[j] = True

            res.append(level[:])
            level.clear()
        return res

    def group_anagrams2(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())

    def group_anagrams3(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for st in strs:
            counts = [0] * 26
            for c in st:
                counts[ord(c) - ord('a')] += 1
            mp[tuple(counts)].append(st)
        return list(mp.values())


class Solution1:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        for word in strs:
            tmp = sorted(word)
            count["".join(tmp)].append(word)
        return list(count.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    s = Solution1()
    print(s.group_anagrams(strs))
