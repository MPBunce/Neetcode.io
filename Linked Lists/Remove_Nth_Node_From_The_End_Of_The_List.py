class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Use a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head

        # Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Calculate the position of the node to be removed
        position = length - n

        # Move to the node just before the one to be removed
        current = dummy
        for n in range(position):
            current = current.next

        # Remove the node
        current.next = current.next.next

        return dummy.next