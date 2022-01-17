# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 2_delete_middle
@time: 2021/12/5 11:32 上午
@desc: 
"""
from typing import Optional
from questions.public import ListNode


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None
        dummy_node = ListNode(0, head)
        slow, fast = dummy_node, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return dummy_node.next
