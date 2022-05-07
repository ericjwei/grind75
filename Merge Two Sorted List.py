class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        s = ListNode()
        temp = s
        while list1.next is not None and list2.next is not None:
            if list1.val > list2.val:
                s.next = list2
                list2 = list2.next
            else:
                s.next = list1
                list1 = list1.next
            s = s.next

        while list1.next is not None:
            s.next = list1
            list1 = list1.next
        
        while list2.next is not None:
            s.next = list2
            list2 = list2.next

        return temp.next

list1 = ListNode()
list1p = list1
for i in [1, 3, 5, 7]:
    list1.next = ListNode(i)
    list1 = list1.next
list2 = ListNode()
list2p = list2
for i in [2, 4, 6, 8]:
    list2.next = ListNode(i)
    list2 = list2.next

s = Solution
result = s.mergeTwoLists(s, list1p.next, list2p.next)
while result.next is not None:
    print(result.val)
    result = result.next
