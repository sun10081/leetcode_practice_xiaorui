# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 23_merge_k_lists
@time: 2021/11/29 11:04 下午
@desc: 
"""
import heapq
from typing import List
from questions.public.ListNode import ListNode


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        """
        顺序合并
        :param lists:
        :return:
        """

        def merge_two_list(l1: ListNode, l2: ListNode) -> ListNode:
            if not l1:
                return l2
            elif not l2:
                return l1
            elif l1.val < l2.val:
                l1.next = merge_two_list(l1.next, l2)
                return l1
            else:
                l2.next = merge_two_list(l1, l2.next)
                return l2

        ans = None
        for node_list in lists:
            ans = merge_two_list(ans, node_list)
        return ans

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        """
        归并合并
        :param lists:
        :return:
        """

        def merge_two_list(l1: ListNode, l2: ListNode) -> ListNode:
            if not l1:
                return l2
            elif not l2:
                return l1
            elif l1.val < l2.val:
                l1.next = merge_two_list(l1.next, l2)
                return l1
            else:
                l2.next = merge_two_list(l1, l2.next)
                return l2

        def merge(l: int, r: int) -> ListNode:
            if l == r:
                return lists[l]
            m = (l + r) // 2
            s1 = merge(l, m)
            s2 = merge(m + 1, r)
            return merge_two_list(s1, s2)

        if not lists:
            return None
        return merge(0, len(lists) - 1)

    def mergeKLists3(self, lists: List[ListNode]) -> ListNode:
        """
        堆
        :param lists:
        :return:
        """
        min_heap = []
        for list_node in lists:
            while list_node:
                heapq.heappush(min_heap, list_node.val)
                list_node = list_node.next
        dummy = ListNode(0)
        point = dummy
        while min_heap:
            point.next = ListNode(val=heapq.heappop(min_heap))
            point = point.next
        return dummy.next


class Solution1:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # 堆
        min_heap = []
        for list_node in lists:
            while list_node:
                heapq.heappush(min_heap, list_node.val)
                list_node = list_node.next
        dummy = ListNode(0)
        cur = dummy
        while min_heap:
            cur.next = ListNode(val=heapq.heappop(min_heap))
            cur = cur.next
        return dummy.next

    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        pass
