from questions.public import ListNode
from collections import defaultdict


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        map方法
        :param headA:
        :param headB:
        :return:
        """
        node_map = defaultdict(int)

        while headB:
            node_map[headB] += 1
            headB = headB.next

        while headA:
            node_map[headA] += 1
            if node_map[headA] == 2:
                return headA
            headA = headA.next

        return None

    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        双指针
        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return None
        pA, pB = headA, headB

        while pA is not pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pB


class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        map
        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return None
        node_map = defaultdict(int)
        while headA:
            node_map[headA] = headA.val
            headA = headA.next
        while headB:
            if headB in node_map:
                return headB
            node_map[headB] = headB.val
            headB = headB.next
        return None

    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        """
        双指针
        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        # 直接用pa pb做循环条件，pa/pb为空则换链表继续跑，不为空直接跑next
        while pA is not pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA

