# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        
        for head in lists:
            while head!=None:
                heapq.heappush(heap, head.val)
                head=head.next
        if not heap:
            return None

        top=ListNode(heapq.heappop(heap), None)
        node=top
        while heap:
            node.next=ListNode(heapq.heappop(heap), None)
            node=node.next
        
        return top