class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        0->1->2->3->4->5->6
        :param head:
        :param n:
        :return:
        """
        tmp_node = ListNode(0, head)
        first = head
        second = tmp_node

        for i in range(n):
            first = first.next
        # first走到尽头 none
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        # return tmp_node.next 直接返回head存在问题，单节点的情况下。。。
        return tmp_node.next


class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        添加前置节点 便于删除节点，且能解决单节点的case
        :param head:
        :param n:
        :return:
        """
        tmp_node = ListNode(0, head)
        fast = head
        slow = tmp_node

        for i in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return tmp_node.next


class Solution3:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        tmp_node = ListNode(0, head)
        slow = fast = tmp_node
        for i in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return tmp_node.next






