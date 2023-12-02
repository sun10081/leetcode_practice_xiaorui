# coding=utf-8

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        left = right = length - 1
        for i in range(length - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                left = i
                break
            if i == 0:
                return nums[::-1]
        for j in range(length - 1, -1, -1):
            if nums[j] > nums[left]:
                right = j
                break
        nums[left], nums[right] = nums[right], nums[left]
        self.reverse_list(nums, left + 1, length - 1)
        return nums

    def reverse_list(self, nums: List[int], left: int, right: int) -> None:
        mid = (left + right + 1) // 2
        k = 0
        for i in range(left, mid):
            nums[i], nums[right - k] = nums[right - k], nums[i]
            k = k + 1

    def nextPermutation2(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


class Solution2:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = n - 2
        # 寻找i
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        # 寻找j
        if i >= 0:
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # 交换i, j
            nums[i], nums[j] = nums[j], nums[i]
        left, right = i + 1, n - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


class Solution3:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        j = n - 1
        while j >= 0:
            if nums[j] > nums[i]:
                break
            j -= 1
        if i >= 0:
            nums[i], nums[j] = nums[j], nums[i]
        left = i + 1
        right = n - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


class Solution4:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        j = n - 1
        while j >= 0:
            if nums[j] > nums[i]:
                break
            j -= 1
        if i >= 0:
            nums[i], nums[j] = nums[j], nums[i]
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


class Solution5:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = n - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        j = n - 1
        while j >= 0:
            if nums[j] > nums[i]:
                break
            j -= 1
        if i >= 0:
            nums[i], nums[j] = nums[j], nums[i]
        left = i + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums


if __name__ == '__main__':
    res = Solution4()
    array = [4, 5, 6, 7, 0, 1, 2]
    res.nextPermutation(array)
    print(array)
