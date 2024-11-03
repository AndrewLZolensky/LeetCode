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
        last_node = None
        next_node = head
        curr_node = None
        while (next_node != None):
            curr_node = next_node
            next_node = curr_node.next
            curr_node.next = last_node
            last_node = curr_node
        head = curr_node
        return head
        