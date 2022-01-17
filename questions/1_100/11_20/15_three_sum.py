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


if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution2()
    start = datetime.datetime.now()
    print(s.threeSum(nums))
    end = datetime.datetime.now()
    method_time = end - start
    print(f"方法耗时为{method_time}")
