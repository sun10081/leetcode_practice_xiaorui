# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 445_add_two_numbers_ii.py
@time: 2023-07-03 16:06:01 
"""
from typing import Optional
from questions.public import ListNode


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse_list(l1)
        l2 = self.reverse_list(l2)
        ans = self.add_two_numbers(l1, l2)
        return self.reverse_list(ans)

    def reverse_list(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        pre, cur = head, head.next
        while cur:
            tmp_node = cur.next
            cur.next = pre
            pre = cur
            cur = tmp_node
        head.next = None
        return pre

    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        val = 0

        while l1 or l2 or val:
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next

            cur.next = ListNode(val % 10)
            cur = cur.next
            val = val // 10

        return dummy.next



