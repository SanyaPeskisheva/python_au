# Math

+[Reverse Integer](#reverse-integer)

+[Palindrome Number](#palindrome-number)

+[Fizz Buzz](#fizz-buzz)

+[Base 7](#base-7)

+[Fibonacci Number](#fibonacci-number)

+[Largest Perimeter Triangle](#largest-perimeter-triangle)

+[Sqrt(x)](#sqrt(x))


## Reverse Integer

https://leetcode.com/problems/reverse-integer/

```python
def reverse(self, x: int) -> int:
        a = 0
        b = x
        if x < 0:
            x = x * (-1)
        while x > 0:
            a = a*10 + x%10
            x = x // 10
        if b < 0:
            a = a*(-1)
        if (a > 2147483647) or (a < -2147483647):
            return 0
        return a
```

## Palindrome Number

https://leetcode.com/problems/palindrome-number/

```python
def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return 0
        else:
            for i in range(0, len(str(x))//2):
                if (str(x))[i] != (str(x))[len(str(x))-i-1]:
                    return 0
            return 1
```

## Fizz Buzz

https://leetcode.com/problems/fizz-buzz/

```python
def fizzBuzz(self, n: int) -> List[str]:
    i = 1
    lst = []       
    while i <= n:
        if (i % 3 == 0) and (i % 5 == 0) :
            lst.append("FizzBuzz")
        elif i % 3 == 0:
            lst.append("Fizz")
        elif i % 5 == 0:
            lst.append("Buzz")
        else:      
            a = str(i)
            lst.append(a)
        i = i + 1   
    return lst
```

## Base 7

https://leetcode.com/problems/base-7/

```python
def convertToBase7(self, num: int) -> str:
        n = ''
        k = 1
        if num < 0:
            num = num * (-1)
            k = -1
        if num == 0:
            return '0'
        if num >0:
            while num != 0:
                n = n + str(num % 7)
                num = num // 7
            n = n[::-1]    
            return(str(int(n)*k))    
```

## Fibonacci Number

https://leetcode.com/problems/fibonacci-number/

```python
def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N ==1:
            return 1
        elif N>1:
            return(self.fib(N-1)+self.fib(N-2))
```

## Largest Perimeter Triangle

https://leetcode.com/problems/largest-perimeter-triangle/

```python
def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse = True)
        for i in range(3,len(A)+1):
            if(A[i-3] < A[i-2] + A[i-1]):
                return sum(A[i-3:i])
        return 0
```

## Sqrt(x)

https://leetcode.com/problems/sqrtx/

```python
def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))
```
