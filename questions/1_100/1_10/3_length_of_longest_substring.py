# coding=utf-8
from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # start, max_length = -1, 0
        # temp_str = ''
        # for i in range(len(s)):
        #     if s[i] in temp_str:
        #         start = i
        #         index = temp_str.find(s[i])
        #         temp_str = temp_str[:index] + s[i] + temp_str[index+1:]
        #     else:
        #         temp_str += s[i]
        #         max_length = max(max_length, i - start)
        # return max_length
        k, res, c_dict = -1, 0, {}
        for i, c in enumerate(s):
            if c in c_dict and c_dict[c] > k:  # 字符c在字典中 且 上次出现的下标大于当前长度的起始下标
                k = c_dict[c]
                c_dict[c] = i
            else:
                c_dict[c] = i
                res = max(res, i - k)
        return res


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        n = len(s)
        counts = defaultdict(int)
        left, right = 0, 0
        ans = 0

        while right < n:
            if counts[s[right]] > 0:
                while counts[s[right]] > 0:
                    counts[s[left]] -= 1
                    left += 1
            counts[s[right]] += 1
            if right - left > ans:
                ans = right - left
            right += 1

        return ans + 1


class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        n = len(s)
        count = defaultdict(int)
        left, right = 0, 0
        ans = 0

        while right < n:
            if count[s[right]] > 0:
                while count[s[right]] > 0:
                    count[s[left]] -= 1
                    left += 1
            count[s[right]] += 1
            right += 1
            if right - left > ans:
                ans = right - left

        return ans


if __name__ == '__main__':
    a = Solution3()
    s = 'dvdf'
    print(a.lengthOfLongestSubstring(s))
