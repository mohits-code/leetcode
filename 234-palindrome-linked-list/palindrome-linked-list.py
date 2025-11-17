# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast.next and fast.next.next:
            slow=slow.next
            fast=fast.next.next
        curr=slow.next
        slow.next=None
        
        prev=None

        while curr:
            t=curr.next
            curr.next=prev
            prev=curr
            curr=t

        
        while prev:
            if prev.val!=head.val:
                return False
            prev=prev.next
            head=head.next
        return True
