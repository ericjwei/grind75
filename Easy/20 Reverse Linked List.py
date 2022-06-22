from __future__ import annotations
class ListNode:
    def __init__(self, val: int = 0, next: ListNode = None):
        self.val = val
        self.next = next

def reverseList(head: ListNode) -> ListNode:
    reverse = head
    reverse.next, head = None, head.next
    while head:
        temp = head.next
        head.next = reverse
        reverse = head
        head = temp
    return reverse

l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l = reverseList(l)
print(l.val)


