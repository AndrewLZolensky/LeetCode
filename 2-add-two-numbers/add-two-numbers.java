/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode head = new ListNode();
        ListNode tail = head;
        int carry = 0;

        while (l1 != null || l2!= null || carry != 0) {

            int d1 = (l1 != null) ? l1.val : 0;
            int d2 = (l2 != null) ? l2.val : 0;
            int nodesum = d1 + d2 + carry;

            int store = nodesum % 10;
            carry = (nodesum - store)/10;

            ListNode newnode = new ListNode(store);
            tail.next = newnode;
            tail = tail.next;

            l1 = (l1 != null) ? l1.next : l1;
            l2 = (l2 != null) ? l2.next : l2;
        }

        head = head.next;
        tail = null;

        return head;
    }
}