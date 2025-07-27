# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #declaring 2 pointers for 2 separate lists
        p1 = list1
        p2 = list2

        #creating the output list
        outlist = ListNode(0)
        current = outlist

        while p1 and p2:
            if p1.val < p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2            
                p2 = p2.next
            current = current.next

        #for the rest of the remaining nodes
        if p1:
            current.next = p1
        else:
            current.next = p2
        return outlist.next

#time: O(n+m)
#space: O(1)