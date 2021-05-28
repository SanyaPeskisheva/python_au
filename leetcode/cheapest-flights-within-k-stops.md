# Graph

+ [Cheapest Flights Within K Stops](#cheapest-flights-within-k-stops)

## Cheapest Flights Within K Stops

https://leetcode.com/problems/cheapest-flights-within-k-stops/

```python
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        G = defaultdict(set)
        for f, t, p in flights: 
            G[f].add((t, p))
            
        P = defaultdict(lambda: inf)
            
        res = inf
        q = [(src, 0, 0)]
        for loc, price, stops in q: 
            if stops > k + 1: 
                break
            if loc == dst: 
                res = min(res, price)
            for to, p in G[loc]: 
                if P[to] > price + p: 
                    P[to] = price + p
                    q.append((to, price + p, stops + 1))
                
        return res if res < inf else -1
```
