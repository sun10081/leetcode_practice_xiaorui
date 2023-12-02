# -*- coding: utf-8 -*-
"""
@author: guoxiaorui
@file: 2
@time: 2023/7/30 11:18 AM
@desc:
"""
from typing import List
from collections import defaultdict, Counter


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        num_cnt = len(count)
        n = len(nums)
        cur_count = defaultdict(int)
        ans = 0
        for i in range(n):
            cur_count[nums[i]] += 1
            if self.check(cur_count, num_cnt):
                ans += 1
            for j in range(i + 1, n):
                cur_count[nums[j]] += 1
                if self.check(cur_count, num_cnt):
                    ans += 1
            cur_count.clear()
        return ans

    def check(self, check_dict, target):
        if len(check_dict) == target:
            return True
        return False


class Solution1:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        m = len(set(nums))
        cnt = Counter()
        ans = left = 0
        for v in nums:  # 枚举子数组右端点 v=nums[i]
            ans += left  # 子数组左端点 < left 的都是合法的
            cnt[v] += 1
            while len(cnt) == m:
                ans += 1  # 子数组左端点等于 left 是合法的
                x = nums[left]
                cnt[x] -= 1
                if cnt[x] == 0:
                    del cnt[x]
                left += 1
        return ans


if __name__ == '__main__':
    s = Solution1()
    nums = [1, 3, 1, 2, 2]
    print(s.countCompleteSubarrays(nums))
