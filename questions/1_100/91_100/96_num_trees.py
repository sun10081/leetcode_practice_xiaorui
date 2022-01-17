# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 96_num_trees
@time: 2021/12/3 3:38 下午
@desc: 
"""


class Solution:
    def numTrees(self, n: int) -> int:
        """
        dp
        假设n个节点存在二叉排序树的个数是G(n)，1为根节点，2为根节点，...，n为根节点，
        当1为根节点时，其左子树节点个数为0，右子树节点个数为n-1，同理当2为根节点时，
        其左子树节点个数为1，右子树节点为n-2，所以可得G(n) = G(0)*G(n-1)+G(1)*(n-2)+...+G(n-1)*G(0)
        :param n:
        :return:
        """
        num_list = [0] * (n + 1)
        num_list[0], num_list[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                num_list[i] += num_list[j - 1] * num_list[i - j]
        return num_list[n]

    def numTrees2(self, n: int) -> int:
        """
        卡特兰数 C(0) = 1,
        C(n) = (4n-2)/(n+1) * C(n-1)
        :param n:
        :return:
        """
        num = 1
        for i in range(1, n + 1):
            num *= (4 * i - 2) / (i + 1)
        return int(num)

    def numTrees3(self, n: int) -> int:
        """
        打表
        :param n:
        :return:
        """
        nums = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670,
                129644790, 477638700, 1767263190]
        return nums[n]


class Solution2:
    def numTrees(self, n: int) -> int:
        """
        dp
        :param n:
        :return:
        """
        nums = [0] * (n + 1)
        nums[0], nums[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                nums[i] += nums[j - 1] * nums[i - j]
        return nums[n]

    def numTrees2(self, n: int) -> int:
        """
        卡特兰数 C(0) = 1,
        C(n) = (4n-2)/(n+1) * C(n-1)
        :param n:
        :return:
        """
        num = 1
        for i in range(1, n + 1):
            num *= (4 * i - 2) / (i + 1)
        return int(num)


if __name__ == '__main__':
    s = Solution2()
    print(s.numTrees2(19))
