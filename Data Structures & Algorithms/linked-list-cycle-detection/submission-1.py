# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers at the start
        slow = head
        fast = head
        
        # 'fast' moves twice as fast, so it will hit the end first
        # We must check 'fast' and 'fast.next' to avoid AttributeError
        while fast and fast.next:
            slow = slow.next          # Moves 1 step
            fast = fast.next.next     # Moves 2 steps
            
            # If they meet, there is a cycle!
            if slow == fast:
                return True
        
        # If 'fast' reaches the end, there is no cycle
        return False