# Design 

+ [Min Stack](#min-stack)

## Min Stack

https://leetcode.com/problems/min-stack/

```python
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            if val <= self.stack[-1][1]:
                self.stack.append((val,val))
            else:
                self.stack.append((val,(self.stack[-1][1])))
        else:
            self.stack.append((val,val))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
```
