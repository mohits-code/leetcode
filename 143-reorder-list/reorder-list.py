# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        def reverse(node):
            if not node or not node.next:
                return node
            new_node=reverse(node.next)
            node.next.next=node
            node.next=None
            return new_node

        second=reverse(slow.next)
        slow.next=None
        first=head
        while second:
            t1=first.next
            t2=second.next
            second.next=t1
            first.next=second
            first=t1
            second=t2

        
    
        
