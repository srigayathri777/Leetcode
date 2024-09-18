import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # Define a wrapper class for ListNode to handle comparisons
        class ListNodeWrapper:
            def __init__(self, node):
                self.node = node
            
            def __lt__(self, other):
                return self.node.val < other.node.val
            
            def __repr__(self):
                return f"ListNodeWrapper({self.node.val})"
        
        # Initialize a min-heap
        heap = []
        
        # Push the head of each list into the heap
        for l in lists:
            if l:
                heapq.heappush(heap, ListNodeWrapper(l))
        
        # Create a dummy head for the result list
        dummy = ListNode()
        current = dummy
        
        # Process the heap until it's empty
        while heap:
            # Pop the smallest element from the heap
            wrapper = heapq.heappop(heap)
            node = wrapper.node
            current.next = node
            current = current.next
            
            # Push the next node of the popped element into the heap if it exists
            if node.next:
                heapq.heappush(heap, ListNodeWrapper(node.next))
        
        # Return the merged list, starting from the next of dummy
        return dummy.next

