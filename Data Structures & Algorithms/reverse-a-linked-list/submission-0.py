# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        current = head

        while current:
            arr.append(current.val)
            current = current.next

        arr.reverse()
        print(arr)

        dummy = ListNode()
        current = dummy

        for item in arr:
            current.next = ListNode(item)
            current = current.next

        return dummy.next

        