/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    let head = new ListNode();
    let tail = head;
    let carry = 0;

    while (l1 != null || l2 != null || carry != 0) {

        // calculate storage and carry variables
        let d1 = (l1 != null) ? l1.val : 0;
        let d2 = (l2 != null) ? l2.val : 0;
        let nodesum = d1 + d2 + carry;
        let store = nodesum % 10;
        carry = (nodesum - store) / 10;

        // allocate new node and link
        let newNode = new ListNode(store);
        tail.next = newNode;
        tail = tail.next;

        // increment l1 and l2
        l1 = (l1 != null) ? l1.next : l1;
        l2 = (l2 != null) ? l2.next : l2;
    }

    head = head.next;

    return head;
};