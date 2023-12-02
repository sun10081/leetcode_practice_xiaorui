# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 300_length_of_LIS
@time: 2021/12/19 1:33 下午
@desc: 
"""
import bisect
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        方法一 dp O(N^2)，借助官方题解图片示意很容易理解，
        :param nums:
        :return:
        """
        n = len(nums)
        dp = [1] * n
        max_len = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_len = max(max_len, dp[i])
        return max_len

    def lengthOfLIS2(self, nums: List[int]) -> int:
        """
        方法二 二分 O(NlogN)
        :param nums:
        :return:
        """
        lis = []
        for num in nums:
            if not lis or num > lis[-1]:
                lis.append(num)
            else:
                loc = bisect.bisect_left(lis, num)
                lis[loc] = num
        return len(lis)


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        dp
        :param nums:
        :return:
        """
        n = len(nums)
        ans = 1
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])
        return ans

    def lengthOfLIS2(self, nums: List[int]) -> int:
        lis = []
        for num in nums:
            if not lis or num > lis[-1]:
                lis.append(num)
            else:
                loc = bisect.bisect_left(lis, num)
                lis[loc] = num
        return len(lis)


class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binary_search_left(x: int):
            left, right = 0, len(lis)
            while left < right:
                mid = (left + right) // 2
                if lis[mid] >= x:
                    right = mid
                elif lis[mid] < x:
                    left = mid + 1
            return left

        lis = []
        tmp_str = []
        for num in nums:
            if not lis or num > lis[-1]:
                lis.append(num)
                tmp_str = lis
            else:
                loc = binary_search_left(num)
                lis[loc] = num
        print(tmp_str)
        return len(lis)


class Solution4:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis = []
        for i in range(n):
            if not lis or nums[i] > lis[-1]:
                lis.append(nums[i])
            else:
                loc = bisect.bisect_left(lis, nums[i])
                lis[loc] = nums[i]
        return len(lis)


class Solution5:
    def lengthOfLIS1(self, nums: List[int]) -> int:
        def dfs(i):
            res = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    res = max(res, dfs(j))
            return res + 1

        n = len(nums)
        ans = 0
        for i in range(n):
            ans = max(ans, dfs(i))
        return ans

    def lengthOfLIS2(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] += 1
        return max(dp)



if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    s = Solution4()
    print(s.lengthOfLIS(nums))
