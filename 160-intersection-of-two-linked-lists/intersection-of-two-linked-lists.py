# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB
        aHasSwitched = False
        bHasSwitched = False
        while a != b:
            if a.next:
                a = a.next
            else:
                if aHasSwitched:
                    return None
                a = headB
                aHasSwitched = True
            if b.next:
                b = b.next
            else:
                if bHasSwitched:
                    return None
                b = headA
                bHasSwitched = True
        return a
        