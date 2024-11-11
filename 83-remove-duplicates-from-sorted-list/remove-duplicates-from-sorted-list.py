# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        r = head
        w = head
        while r:
            if r.val == w.val:
                r = r.next
                w.next = None
            else:
                w.next = r
                w = w.next
                r = r.next
        return head
        