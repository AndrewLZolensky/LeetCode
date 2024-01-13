/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* head = malloc(sizeof(struct ListNode));
    if (head == NULL) {
        return NULL;
    }
    struct ListNode* tail = head;
    int carry = 0;

    while (l1 != NULL || l2 != NULL || carry != 0) {
        int d1 = (l1 != NULL) ? l1->val : 0;
        int d2 = (l2 != NULL) ? l2->val : 0;

        int nodesum = d1 + d2 + carry;
        int store = nodesum % 10;
        carry = (nodesum - store) / 10;

        struct ListNode* newNode = malloc(sizeof(struct ListNode));
        if (newNode == NULL) {
            return NULL;
        }

        newNode->val = store;
        newNode->next = NULL;
        tail->next = newNode;
        tail = tail->next;

        l1 = (l1 != NULL) ? l1->next : l1;
        l2 = (l2 != NULL) ? l2->next : l2;
    }

    struct ListNode* toss = head;
    head = head->next;
    free(toss);

    return head;
}