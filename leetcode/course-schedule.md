# Graph

+ [Course Schedule](#course-schedule)

## Course Schedule

https://leetcode.com/problems/course-schedule/ 

```python
def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    g = defaultdict(list)
    for item in prerequisites:
        a = item[0]
        b = item[1]
        g[b].append(a)  
    vis = [-1 for i in range(numCourses)]
        
def dfs(root):
    vis[root] = 1
    for adj in g[root]:
        if(vis[adj]==-1):
            if(dfs(adj)):
                return True
        elif(vis[adj]==1):
            return True
    vis[root]=2
    return False
```
