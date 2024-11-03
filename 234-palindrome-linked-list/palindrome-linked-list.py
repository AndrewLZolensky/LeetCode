# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """

        if head == None or head.next == None:
            return True
        one = head
        two = head
        stack = []
        while two and two.next:
            stack.append(one.val)
            one = one.next
            two = two.next.next
        
        if two:
            one = one.next
        
        while one:
            el = stack.pop()
            if el != one.val:
                return False
            one = one.next
        
        return True

        