# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        store = 0
        head = None
        ptr = head
        while (l1 is not None or l2 is not None):
            if (head is None):
                head = ListNode()
                ptr = head
            else:
                ptr.next = ListNode()
                ptr = ptr.next
            if (l1 is None):
                nodesum = l2.val + carry
                store = nodesum % 10
                carry = (nodesum - store)/10
                l2 = l2.next
            elif (l2 is None):
                nodesum = l1.val + carry
                store = nodesum % 10
                carry = (nodesum - store)/10
                l1 = l1.next
            else:
                nodesum = l1.val + l2.val + carry
                store = nodesum % 10
                carry = (nodesum - store)/10
                l1 = l1.next
                l2 = l2.next
            ptr.val = store
        if (carry == 1):
            ptr.next = ListNode()
            ptr = ptr.next
            ptr.val = carry
        
        return head
