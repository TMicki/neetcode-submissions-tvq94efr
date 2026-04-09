# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
    
        while curr:
        # 1. Save the next node (so we don't lose the rest of the list)
            next_node = curr.next
        
        # 2. Reverse the link
            curr.next = prev
        
        # 3. Move the pointers forward for the next iteration
            prev = curr
            curr = next_node

    # At the end, curr is None and prev is the new head
        return prev