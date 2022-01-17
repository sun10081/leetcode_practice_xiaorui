# coding=utf-8

from questions.public import ListNode


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast, tmp = head, head, head
        while True:
            if fast is None or fast.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        while tmp != slow:
            tmp = tmp.next
            slow = slow.next
        return slow


class Solution2:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        while True:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                break

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
