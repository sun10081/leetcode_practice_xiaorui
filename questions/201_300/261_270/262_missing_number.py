# coding=utf-8

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        方法一 异或
        方法二 求和公式
        :param nums:
        :return:
        """
        # xor = 0
        # for num in nums:
        #     xor = xor ^ num
        # for num in range(len(nums) + 1):
        #     xor = xor ^ num
        # return xor

        nums_len = len(nums)
        target_sum = (1 + nums_len) * nums_len // 2
        array_sum = sum(nums)
        return target_sum - array_sum


if __name__ == '__main__':
    nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    s = Solution()
    print(s.missingNumber(nums))
