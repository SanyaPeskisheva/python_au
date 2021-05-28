# Graph

+ [Course Schedule II](#course-schedule-ii)

## Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

```python
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        sortedOrder = []
        
        if numCourses <= 0:
            return sortedOrder
        
        inDegree = {i:0 for i in range(numCourses)}
        adMatrix = {i:[] for i in range(numCourses)}
        
        for edge in prerequisites:
            parent, child = edge[1], edge[0]
            inDegree[child] += 1
            adMatrix[parent].append(child)
        
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        while sources:
            source = sources.popleft()
            sortedOrder.append(source)
            for child in adMatrix[source]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        if len(sortedOrder) != numCourses:
            return []
        
        return sortedOrder
```
