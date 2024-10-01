class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Traverse both lists
        while l1 or l2 or carry:
            # Get the current values from the lists, if present
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10  # carry for the next iteration
            total = total % 10  # the current digit to store
            
            # Create a new node for the result
            current.next = ListNode(total)
            current = current.next
            
            # Move to the next nodes, if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next  # Return the next node as the dummy is a placeholder

        