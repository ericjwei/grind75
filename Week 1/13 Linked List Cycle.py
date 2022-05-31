from __future__ import annotations
class ListNode:
    def __init__(self, x: int, next: ListNode = None):
        self.val = x
        self.next = next

def hasCycle(head: ListNode) -> bool:
    fast = slow = head
    
    while True:
        if not (fast.next and fast.next.next):
            return False
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
        
def createlist(arr: list, loop: int) -> ListNode:
    p = l = head = ListNode(arr[0])
    for i in arr[1:]:
        p.next = ListNode(i)
        p = p.next
    if loop > -1:
        for _ in range(loop):
            l = l.next
        p.next = l

    return head

head = createlist([3,2,0,-4], -1)
print(hasCycle(head))



