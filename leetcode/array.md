# Array

+[Max Consecutive Ones](#max-consecutive-ones)

+[Reshape the Matrix](#reshape-the-matrix)

+[Image Smoother](#image-smoother)

+[Flipping an Image](#flipping-an-image)

+[Transpose Matrix](#transpose-matrix)

+[Move Zeroes](#move-zeroes)

+[Squares of a Sorted Array](#squares-of-a-sorted-array)

## Max Consecutive Ones

https://leetcode.com/problems/max-consecutive-ones/

```python
def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                if count > mx:
                    mx = count
                count = 0
        if count > mx:
            mx = count
        return mx
```

## Reshape the Matrix

https://leetcode.com/problems/reshape-the-matrix/

```python
def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != (len(nums)*len(nums[0])) or not nums:
            return nums
        q = []
        for i in range(len(nums)):
            for n in range(len(nums[i])):
                q.append(nums[i][n])
        newMatrix = [[0 for i in range(c)] for n in range(r)]
        for i in range(len(newMatrix)):
            for n in range(len(newMatrix[i])):
                newMatrix[i][n] = q.pop(0)
        return newMatrix
```

## Image Smoother

https://leetcode.com/problems/image-smoother/

```python
def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        rows = len(M)
        cols = len(M[0])
        res = [[0]*cols for _ in range(0, rows)]
        for row in range(0, rows):
            for col in range(0, cols):
                num = 0
                denom = 0
                for r in range(row - 1, row + 2):
                    for c in range(col - 1, col  + 2):
                        if r >= 0 and r < rows and c >= 0 and c < cols:
                            num += M[r][c]
                            denom += 1
                res[row][col] = math.floor(num/denom)
        return res
```

## Flipping an Image

https://leetcode.com/problems/flipping-an-image/

```python
 def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[0 if i == 1 else 1 for i in reversed(r)] for r in A]
```

## Transpose Matrix

https://leetcode.com/problems/transpose-matrix/

```python
def transpose(self, A: List[List[int]]) -> List[List[int]]:
        newMatrix = [[0]*len(A) for i in range(len(A[0]))]
        for i in range(len(A[0])):
            for n in range(len(A)):
                newMatrix[i][n] = A[n][i]
        return newMatrix
```

## Move Zeroes

https://leetcode.com/problems/move-zeroes/

```python
def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        while 0 in nums:
            nums.remove(0)
            count += 1
        for i in range(count):
            nums.append(0)
        return nums
```

## Squares of a Sorted Array

https://leetcode.com/problems/squares-of-a-sorted-array/

```python
def sortedSquares(self, nums: List[int]) -> List[int]:
        n = 0
        m = len(nums)-1
        res = [None]*len(nums)
        i = len(nums)-1
        while n <= m:
            if abs(nums[i]) > abs(nums[m]):
                res[i] = nums[n]**2
                n += 1
                i -= 1
            else:
                res[i] = nums[m]**2
                m -= 1
                i -= 1
        return sorted(res)
```
