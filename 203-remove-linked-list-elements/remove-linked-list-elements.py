# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        if head == None:
            return None

        # delete beginning sequence of nodes with val if present
        while head.val == val:
            head = head.next
            if head == None:
                return None
        
        # handle rest of nodes
        temp = head
        while temp != None and temp.next != None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
            
        return head