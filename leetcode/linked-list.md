# Linked List

+[Reverse Linked List](#reverse-linked-list)

+[Middle of the Linked List](#middle-of-the-linked-list)

+[Palindrome Linked List](#palindrome-linked-list)

+[Merge Two Sorted Lists](#merge-two-sorted-lists)

+[Remove Nth Node From End of List](#remove-nth-node-from-end-of-list)

+[Linked List Cycle II](#linked-list-cycle-II)

+[Linked List Cycle](#linked-list-cycle)

+[Reorder List](#reorder-list)

+[Intersection of Two Linked Lists](#intersection-of-two-linked-lists)

+[Sort List](#sort-list)

## Reverse Linked List

https://leetcode.com/problems/reverse-linked-list/

```python
def reverseList(self, head: ListNode) -> ListNode:
        if (head == None or head.next == None):
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
```

## Middle of the Linked List

https://leetcode.com/problems/middle-of-the-linked-list/

```python
def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```

## Palindrome Linked List

https://leetcode.com/problems/palindrome-linked-list/

```python
def isPalindrome(self, head: ListNode) -> bool:
        one = head
        two = head
        while two != None and two.next != None:
            one = one.next
            if two.next == None:
                two = two.next
            else:
                two = two.next.next
        n = 0;
        sch = head;
        while sch != None:
            n = n + 1
            sch = sch.next
        if n%2 != 0:
            one = one.next
        cur = one
        Next = None
        prev = None
        while cur != None:
            Next = cur.next
            cur.next = prev
            prev = cur
            cur = Next
        one = prev
        flag = 1
        while one != None:
            if head.val != one.val:
                flag = 0
            head = head.next
            one = one.next
        return flag
```

## Merge Two Sorted Lists

https://leetcode.com/problems/merge-two-sorted-lists/

```python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        newlst = head
        if l1 is None:
            head.next = l2
        elif l2 is None:
            head.next = l1
        while l1 and l2 is not None:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
            if l1 is not None:
                head.next = l1
            else:
                head.next = l2
        return newlst.next
```

## Remove Nth Node From End of List

https://leetcode.com/problems/remove-nth-node-from-end-of-list/

```python
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head
```

## Linked List Cycle II

https://leetcode.com/problems/linked-list-cycle-ii/

```python
def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                fast = head
                while fast != slow:
                    fast = fast.next
                    slow = slow.next
                return fast
        return None
```

## Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

```python
def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
```

## Reorder List

https://leetcode.com/problems/reorder-list/

```python
def reorderList(self, head: ListNode) -> None:
        if head == None or head.next == None:
            return True
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        middle = slow
        
        prev = None
        cur = middle
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        head2 = prev
        
        res = head
        while head and head2:
            next1 = head.next
            next2 = head2.next
            head.next = head2
            head2.next = next1
            last = head2
            head = next1
            head2 = next2
        last.next = None
        return res
```

## Intersection of Two Linked Lists

https://leetcode.com/problems/intersection-of-two-linked-lists/

```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        if headA is None or headB is None:
            return None
        while a != b :
            a = headB if a == None else a.next
            b = headA if b == None else b.next
        return a
```

## Sort List

https://leetcode.com/problems/sort-list/

```python
def sortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        r = None
        slow = head
        fast = head
        while fast and fast.next:
            r = slow
            slow = slow.next
            fast = fast.next.next
        r.next = None
        return self.merge(self.sortList(head), self.sortList(slow))
    
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = output = ListNode()
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 == None:
            cur.next = l2
        if l2 == None:
            cur.next = l1
        return output.next
```
