# coding=utf-8

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        nums = len(height)
        left_max_array = [height[0]] + [0] * (nums - 1)
        for i in range(1, nums):
            left_max_array[i] = max(left_max_array[i - 1], height[i])

        right_max_array = [0] * (nums - 1) + [height[nums - 1]]
        for i in range(nums - 2, -1, -1):
            right_max_array[i] = max(height[i], right_max_array[i + 1])

        total_array = [0] * nums
        for i in range(nums):
            total_array[i] = min(left_max_array[i], right_max_array[i]) - height[i]
        return sum(total_array)


class Solution1:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        n = len(height)

        for i in range(n):
            while stack and height[stack[-1]] < height[i]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                cur_width = i - left - 1
                cur_height = min(height[left], height[i]) - height[top]
                ans += cur_width * cur_height
            stack.append(i)
        return ans


class Solution2:
    def trap1(self, height: List[int]) -> int:
        # 动态规划
        n = len(height)
        left_max = [height[0]] + [0] * (n - 1)
        right_max = [0] * (n - 1) + [height[-1]]

        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        dp = [0] * n
        for i in range(n):
            dp[i] = min(left_max[i], right_max[i]) - height[i]
        return sum(dp)

    def trap2(self, height: List[int]) -> int:
        # 单调栈
        n = len(height)
        stack = []
        ans = 0

        for i in range(n):
            while stack and height[stack[-1]] <= height[i]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                cur_width = i - left - 1
                cu_height = min(height[left], height[i]) - height[top]
                ans += cur_width * cu_height
            stack.append(i)
        return ans


class Solution3:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        pre_max = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])
        suf_max = [0] * (n - 1) + [height[-1]]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(height[i], suf_max[i + 1])
        for i in range(n):
            ans += min(pre_max[i], suf_max[i]) - height[i]
        return ans


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    s = Solution3()
    print(s.trap(height))
