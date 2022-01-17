# coding=utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return

        linear_list = list()
        node = head
        while node:
            linear_list.append(node)
            node = node.next

        begin, end = 0, len(linear_list) - 1
        while begin < end:
            linear_list[begin].next = linear_list[end]
            begin += 1
            if begin == end:
                break
            linear_list[end].next = linear_list[begin]
            end -= 1

        linear_list[begin].next = None

