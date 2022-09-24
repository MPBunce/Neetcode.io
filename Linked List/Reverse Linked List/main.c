/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* reverseList(struct ListNode* head){

    struct ListNode* headRef = head;
    
    struct ListNode* prev = NULL;
    struct ListNode* current = headRef; 
    struct ListNode* next = NULL;
    
    while(current != NULL){
        
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
        
    }
    headRef = prev;
    
    return headRef;
    
}