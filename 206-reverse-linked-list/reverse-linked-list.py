# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        last = None
        curr_node = None
        next_node = head
        while (next_node != None):
            curr_node = next_node
            next_node = curr_node.next
            curr_node.next = last
            last = curr_node
        head = curr_node
        return head
        
        
        