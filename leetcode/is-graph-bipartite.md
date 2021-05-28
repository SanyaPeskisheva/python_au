# Graph

+ [Is Graph Bipartite?](#is-graph-bipartite)

## Is Graph Bipartite?

https://leetcode.com/problems/is-graph-bipartite/

```python
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for node in range(len(graph)): 
            if node not in color:
                stack = [node]
                color[node] = 0 
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            if color[node] == 0: 
                                color[nei] = 1
                            elif color[node] == 1:
                                color[nei] = 0
                            stack.append(nei)
                        else:
                            if color[nei] == color[node]:
                                return False
        return True
```
