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
        new_head = self.reverseListHelper(head)
        return new_head
        
    def reverseListHelper(self, node):
        if (node == None):
            return None
        elif (node.next == None):
            return node
        else:
            new_head = self.reverseListHelper(node.next)
            node.next.next = node
            node.next = None
            return new_head
        
        
        