# Design

+ [Implement Stack using Queues](#implement-stack-using-queues)

## Implement Stack using Queues

https://leetcode.com/problems/implement-stack-using-queues/

```python
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = deque([])

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.queue1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue1.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.queue1[-1] 

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self.queue1
```
