# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ret = ListNode()
        r=ret
        while list1 and list2:
            if list1.val<=list2.val:
                r=ListNode(list1.val)
                list1=list1.next
            else:
                r=ListNode(list2.val)
                list2=list2.next
            r=r.next
        
        # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ret = ListNode()
        r = ret
        
        while list1 and list2:
            if list1.val <= list2.val:
                r.next = list1
                list1 = list1.next
            else:
                r.next = list2
                list2 = list2.next
            r = r.next
        
        if list1:
            r.next = list1
        else:
            r.next = list2
        
        return ret.next 
