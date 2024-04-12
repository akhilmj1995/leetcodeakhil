# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        m=list1
        for i in range(a-1):
            m=m.next
        k=m.next
        m.next=list2
        for i in range(b-a+1):
            k=k.next
        while list2.next:
            list2=list2.next
        list2.next=k
        return list1

        