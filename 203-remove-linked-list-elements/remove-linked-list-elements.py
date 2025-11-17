# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        x=dummy
        while x and x.next:
            if x.next.val==val:
                x.next=x.next.next
            else:
                x=x.next
        return dummy.next
