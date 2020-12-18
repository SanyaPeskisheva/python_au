# String

+[Valid Anagram](#valid-anagram)

+[Reverse String](#reverse-string)

+[Reverse Vowels of a String](#reverse-vowels-of-a-string)

+[Reverse Words in a String III](#reverse-words-in-a-string-III)

+[To Lower Case](#to-lower-case)

## Valid Anagram

https://leetcode.com/problems/valid-anagram/

```python
def isAnagram(self, s: str, t: str) -> bool:
         return Counter(s) == Counter(t)
```

## Reverse String

https://leetcode.com/problems/reverse-string/

```python
def reverseString(self, s: List[str]) -> None:
        for i in range(len(s)//2):
            t = s[len(s)- 1 - i]
            s[len(s) - 1 - i] = s[i]
            s[i] = t
        return s
```

## Reverse Vowels of a String

https://leetcode.com/problems/reverse-vowels-of-a-string/

```python
def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        vowels_in_s = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in vowels:
                print(s[i])
                vowels_in_s.append(s[i])
                s[i] = "*"
        reverse_vowels_in_s = vowels_in_s[::-1]
        count = 0 
        for i in range(len(s)):
            if s[i] == "*":
                s[i] = reverse_vowels_in_s[count]
                count += 1 
        s = "".join(s)
        return s
```

## Reverse Words in a String III

https://leetcode.com/problems/reverse-words-in-a-string-iii/

```python
def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            s[i] = list(s[i])
            for j in range(len(s[i])):
                s[i].insert(j, s[i][len(s[i])-1])
                del s[i][len(s[i])-1]
            s[i] = ''.join(s[i])
        s = ' '.join(s)
        return s
```

## To Lower Case

https://leetcode.com/problems/to-lower-case/

```python
def toLowerCase(self, str: str) -> str:
        return(str.lower())
```
