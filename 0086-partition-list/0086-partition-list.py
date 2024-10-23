# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummyLeft=  ListNode() 
        dummyRight = ListNode() 

        leftPoint, rightPoint= dummyLeft, dummyRight  

        while head:

            if  head.val < x:
                leftPoint.next = head
                leftPoint =  leftPoint.next

            else:
                rightPoint.next =  head
                rightPoint= rightPoint.next

           

            head = head.next

        leftPoint.next =  dummyRight.next
        rightPoint.next = None
   
        return dummyLeft.next
       

        