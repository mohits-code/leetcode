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
        '''num1=0
        c=0
        while l1 != None:
            num1=num1 + l1.val*10**c
            l1=l1.next
        
        num2=0
        c=0
        while l2 != None:
            num2=num2 + l2.val*10**c
            l2=l2.next
        int(ans) = num1+num2

        node = ListNode(ans%10)
        n=node.next
        ans = ans/10
       
        return None
'''
        node = ListNode(0)
        n=node
        c=0
        while l1!= None or l2!=None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            s = c + x + y
            c=s//10
            n.next = ListNode(s%10)
            
            n=n.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if c!=0:
            n.next = ListNode(c)
        return node.next


        
        
