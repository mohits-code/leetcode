# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return 
        if head.next==None:
            return head

        newNode = None
        curr=head
        while curr!=None:
            temp=newNode
            newNode= ListNode(curr.val, temp)
            curr=curr.next
        return newNode