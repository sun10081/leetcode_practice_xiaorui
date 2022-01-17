# coding=utf-8

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head

        head.next = self.removeElements(head.next, val)
        if head.val == val:
            next_node = head.next
        else:
            next_node = head
        return next_node

