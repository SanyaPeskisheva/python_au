# Graph

+ [Number of Islands](#number-of-islands)

## Number of Islands

https://leetcode.com/problems/number-of-islands/

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def surroundCheck(binaryMatrix,i,j):
            lr=len(binaryMatrix)-1 
            lc=len(binaryMatrix[0])-1


            if binaryMatrix[i][j]=="0":
                return
            binaryMatrix[i][j]="0" 


            if (i+1) <= lr:
                 surroundCheck(binaryMatrix,i+1,j)

            if (j+1) <= lc:
                surroundCheck(binaryMatrix,i,j+1)

            if (i-1) >= 0:
                surroundCheck(binaryMatrix,i-1,j) 

            if (j-1) >= 0:
                surroundCheck(binaryMatrix,i,j-1)  

        numIsland=0
        for i in range(len(grid)):
            for j in  range(len(grid[0])):

                if grid[i][j]=="1":
                    surroundCheck(grid,i,j)
                    numIsland+=1

        return  numIsland
```
