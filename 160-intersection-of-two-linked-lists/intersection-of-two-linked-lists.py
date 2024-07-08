# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (headA == None or headB == None):
            return None
        la = getL(headA)
        lb = getL(headB)
        
        while la>lb:
             headA=headA.next
             la-=1
        while lb>la:
             headB=headB.next
             lb-=1
        
        while headA != None:
            if headA== headB:
                return headA
            headA=headA.next
            headB=headB.next
        return None

def getL(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length
