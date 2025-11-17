# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        x=head
        count=0
        while x:
            x=x.next
            count+=1

        count-=n
        x=dummy

        while count>0:
            x=x.next
            count-=1

        x.next=x.next.next

        return dummy.next