# coding=utf-8

from questions.public import ListNode


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True


class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        if slow is fast:
            return True
        while slow != fast and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    def hasCycle2(self, head: ListNode) -> bool:
        """
        精简版
        :param head:
        :return:
        """
        if not head or not head.next:
            return False
        # 循环条件 所以要快一步
        slow = head
        fast = head.next
        while slow is not fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
