import datetime
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # 排序 剔除重复元素,排序时间复杂度伟O(NlogN), 小于N*N，不会影响整体复杂度
        nums.sort()
        ans = list()

        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            target = -nums[first]
            third = n - 1
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                # 如果指针重合，随着 b 后续的增加
                # 就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans


class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        if not nums:
            return ans
        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            target = - nums[first]
            third = n - 1
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:
                    break
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans


class Solution3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            target = -nums[first]
            third = n - 1
            for second in range(first + 1, third):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third - 1 and nums[second] + nums[third - 1] >= target:
                    third -= 1
                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])
        return ans


class Solution4:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        for first in range(len(nums)):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = n - 1
            for second in range(first + 1, third):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                while second < third and nums[first] + nums[second] + nums[third] > 0:
                    third -= 1
                if second == third:
                    break
                if nums[first] + nums[second] + nums[third] == 0:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        for first in range(0, n - 2):
            if nums[first] > 0:
                return ans
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            l, r = first + 1, n - 1
            while l < r:
                cur_sum = nums[l] + nums[r] + nums[first]

                if cur_sum == 0:
                    ans.append([nums[first], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while r > l and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif cur_sum > 0:
                    r -= 1
                else:
                    l += 1

        return ans


class Solution5:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 2):
            x = nums[i]
            if x + nums[i + 1] + nums[i + 2] > 0:
                break
            if x + nums[-1] + nums[-2] < 0:
                continue
            if i > 0 and x == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                if x + nums[l] + nums[r] > 0:
                    r -= 1
                elif x + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    ans.append([x, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
        return ans


if __name__ == '__main__':
    nums = [-2, 0, 0, 2, 2]
    s = Solution5()
    start = datetime.datetime.now()
    print(s.threeSum(nums))
    end = datetime.datetime.now()
    method_time = end - start
    print(f"方法耗时为{method_time}")
