# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1 and not list2: # catch empty lists
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        
        # if we get here, both lists have at least one element
        head = None
        curr = None
        while list1 and list2: # while there are nodes left
            # compare list1 and list2
            val1 = list1.val
            val2 = list2.val
            # if list1 is bigger, make it curr.next -> if head is none, make it curr & head
            if val1 < val2:
                if not head:
                    head = list1
                    curr = head
                    list1 = list1.next
                else:
                    curr.next = list1
                    list1 = list1.next
                    curr = curr.next
            else:
                if not head:
                    head = list2
                    curr = head
                    list2 = list2.next
                else:
                    curr.next = list2
                    list2 = list2.next
                    curr = curr.next
        
        if not list2: # if there are nodes left in the non-empty list, add them
            while list1:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
        if not list1:
            while list2:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
        curr.next = None
        
        return head

        