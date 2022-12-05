# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listLen = 0
        node = head
        while node is not None:
            listLen += 1
            node = node.next

        node = head
        for i in range(listLen // 2):
            node = node.next
        
        return node
