# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        node = ListNode(0)
        n=node
        c=0
        
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = c + x + y
            
            c=s//10
            n.next = ListNode(s%10)
            
            n=n.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if c!=0:
            n.next = ListNode(c)
        
        return node.next


        
        
