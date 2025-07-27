# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #counting the total nodes
        count = 0 
        current = head
        while current:
            count +=1
            current = current.next

        # Find out the target node to delete
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        target = count-n
        for i in range(target):
            current = current.next

        current.next = current.next.next
        return dummy.next  

        #time complexity: O(n)
        #space complexity: O(1)