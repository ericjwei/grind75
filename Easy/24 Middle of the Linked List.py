from __future__ import annotations
class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next

def middleNode(head: ListNode) -> ListNode:
    fast = slow = head
    while True:
        if fast.next:
            slow = slow.next
        else:
            return slow
        if fast.next.next:
            fast = fast.next.next
        else:
            return slow

l = ListNode(1)
print(middleNode(l).val)