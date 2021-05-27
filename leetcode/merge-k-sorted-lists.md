# Linked List

+ [Merge K Sorted Lists](#merge-k-sorted-lists)

## Merge K Sorted Lists

https://leetcode.com/problems/merge-k-sorted-lists/

```python
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]
    mid = len(lists) // 2
    l = self.mergeKLists(lists[:mid]), 
    r = self.mergeKLists(lists[mid:])
    return self.merge(l, r)
    
def merge(self, l, r):
    prev = head = ListNode()
    while l and r:
        if l.val < r.val:
            head.next = l
            l = l.next
        else:
            head.next = r
            r = r.next
        head = head.next
    head.next = l or r
    return prev.next
```
