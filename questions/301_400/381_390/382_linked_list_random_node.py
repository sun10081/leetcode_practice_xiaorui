# -*- coding:utf-8 -*-
"""
@author: guoxiaorui
@file: 382_linked_list_random_node.py
@time: 2022-01-16 20:34:02 
"""
import random
from typing import Optional
from questions.public.ListNode import ListNode


class Solution:
    # 空间换时间
    def __init__(self, head: Optional[ListNode]):
        self.val_list = []
        while head:
            self.val_list.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.val_list)


class Solution2:
    # 蓄水池
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        ans = 0
        index = 1
        node = self.head
        while node:
            if random.randrange(start=0, stop=index) == 0:
                ans = node.val
            index += 1
            node = node.next
        return ans


