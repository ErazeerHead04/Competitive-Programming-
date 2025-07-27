# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def getsum(head):
            num = 0
            place = 1
            while head:
                num += head.val*place
                place *= 10
                head = head.next
            return num
        

        def totaltolist(num):
            if num==0:
                return ListNode(0)
            head = None
            current = None

            while num>0:
                digit = num%10
                output_node = ListNode(digit)
                
                if head is None:
                    head = output_node
                else:
                    current.next = output_node
                current = output_node
                num = num//10
            return head
        total = (getsum(l1)+getsum(l2))
        retun totaltolist(total)
        
