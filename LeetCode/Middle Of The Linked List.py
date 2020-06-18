# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self,head):
        l=1
        temp = head
        while(temp.next):
            l+=1
            temp=temp.next
        return l
    def middleNode(self, head: ListNode) -> ListNode:
        l = self.length(head)
        i=1
        while(i!=l//2+1):
            head = head.next
            i+=1
        return hea
