from questions.public.ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = ListNode()
        carry = val = 0

        while carry or l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            tail.next = ListNode(val)
            tail = tail.next
        return head.next


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        第二遍刷 初始化head tail要注意
        :param l1:
        :param l2:
        :return:
        """
        head, tail = ListNode(), ListNode()
        head.next = tail
        carry, val = 0, 0

        while carry or l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            carry, val = divmod(val, 10)
            tail.next = ListNode(val)
            tail = tail.next
        return head.next


if __name__ == '__main__':
    a, b = divmod(10, 3)
    print(a)
    print(b)
