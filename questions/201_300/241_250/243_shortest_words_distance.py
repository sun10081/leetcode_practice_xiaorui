# coding=utf-8

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        cur_node = head
        while cur_node is not None:
            vals.append(cur_node.val)
            cur_node = cur_node.next
        return vals == vals[::-1]
