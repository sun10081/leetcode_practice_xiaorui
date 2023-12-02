from questions.public import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        迭代
        :param head:
        :return:
        """
        pre = None
        cur = head
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        """
        递归
        :param head:
        :return:
        """
        if head is None or head.next is None:
            return head
        new_head = self.reverseList2(head.next)
        head.next.next = head
        head.next = None
        return new_head


class Solution2:
    """
    二刷
    """

    def reverseList_iteration(self, head: ListNode) -> ListNode:
        """
        iteration
        :param head:
        :return:
        """
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre

    def reverse_list_recursion(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        # 向下一个节点递归
        new_head = self.reverse_list_recursion(head.next)
        head.next.next = head
        head.next = None
        return new_head


class Solution3:
    def reverseListIteration(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, cur = None, head
        next = cur.next

        while cur and cur.next:
            cur.next = pre
            pre = cur
            cur = next
            next = cur.next

        return pre

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head


class Solution4:
    def reverseListIteration(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre, cur = None, head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre


class Solution5:
    def reverseListIteration(self, head: ListNode) -> ListNode:
        """
        迭代
        :param head:
        :return:
        """
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

    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        tail = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return tail

