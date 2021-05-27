# Graph

+ [Maximum Depth Of N-ary Tree](#maximum-depth-of-n-ary-tree)

## Maximum Depth Of N-ary Tree

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/ 

```python
def maxDepth(self, root: 'Node') -> int:
    if not root:
        return 0
    queue = [root]
    depth = 0
    while queue:
        for i in range(len(queue)):
            node = queue.pop(0)
            if node.children:
                for child in node.children:
                    queue.append(child)
        depth += 1
    return depth
```
