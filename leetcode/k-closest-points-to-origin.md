# Math

+ [K Closest Points To Origin](#k-closest-point-to-origin)
  
## K Closest Point To Origin
  
https://leetcode.com/problems/k-closest-points-to-origin/ 

``` python
def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
    arraydist = []
    arraydistok = []
    for point in points:
        distance = math.sqrt(point[0]**2 + point[1]**2)
        arraydist.append((distance, point))
        
    arraydist = sorted(arraydist, key=lambda point: point[0])
    
    for i in range(k):
        arraydistok.append(arraydist[i][1])
        
    return arraydistok
```
