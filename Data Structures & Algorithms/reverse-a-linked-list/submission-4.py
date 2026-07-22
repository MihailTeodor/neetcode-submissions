# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        stack = []

        stack.append(head)

        while head.next:
            stack.append(head.next)
            head = head.next
        
        head = pointer = stack.pop()
        while stack:
            pointer.next = stack.pop()
            pointer = pointer.next

        pointer.next = None

        return head


        