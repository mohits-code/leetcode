# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        head1=list1
        head2=list2
        newHead=ListNode()
        curr=newHead
        while head1!=None and head2!=None:
            if head1.val>=head2.val:
                curr.next=ListNode(head2.val,None)
                head2=head2.next
            else:
                curr.next=ListNode(head1.val,None)
                head1=head1.next
            curr=curr.next
        if head1!=None:
            curr.next=head1
        elif head2!=None:
            curr.next=head2
        return newHead.next

            
            
        