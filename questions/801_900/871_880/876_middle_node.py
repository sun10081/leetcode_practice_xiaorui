# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 871_880
@time: 2021/12/17 3:56 下午
@desc: 
"""
from questions.public import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head.next:
            return head
        dummy = ListNode(val=0, next=head)
        slow, fast = dummy, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.next
