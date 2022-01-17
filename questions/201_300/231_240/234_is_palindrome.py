from questions.public import ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        数组存储
        :param head:
        :return:
        """
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next
        return vals == vals[::-1]

    def isPalindrome2(self, head: ListNode) -> bool:
        if not head:
            return True
        half_node = self.half_of_list_node(head)
        reversed_head = self.reverse_list_node(half_node.next)

        res = True
        p_start = head
        p_half = reversed_head
        while res and p_half:
            if p_start.val != p_half.val:
                res = False
            p_start = p_start.next
            p_half = p_half.next
        half_node.next = self.reverse_list_node(reversed_head)
        return res

    def half_of_list_node(self, head: ListNode) -> ListNode:
        fast = slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list_node(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre


class Solution2:
    def isPalindrome1(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]

    def isPalindrome2(self, head: ListNode) -> bool:
        if not head:
            return True

        half_node = self.half_of_list_node(head)
        reverse_head = self.reverse_list_node(half_node.next)

        res = True
        # 如果需要还原链表 需要保存half_node reverse_head节点
        # half_node.next = self.reverse_list_node(reversed_head)
        while res and reverse_head:
            if head.val != reverse_head.val:
                res = False
            head = head.next
            reverse_head = reverse_head.next
        return res

    def half_of_list_node(self, head: ListNode) -> ListNode:
        fast = slow = head
        # 这里注意 fast要达到最后一个 所以是fast.next, fast.next.next
        # 必须都不为空 用and
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list_node(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = pre
            pre = cur
            cur = next_node
        return pre
