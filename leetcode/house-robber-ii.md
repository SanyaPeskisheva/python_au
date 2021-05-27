# Dynamic programming

+ [House Robber II](#house-robber-ii)

## House Robber II

https://leetcode.com/problems/house-robber-ii/ 

```python
def rob1(self, nums):
    rob1, rob2 = 0, 0
    for num in nums:
        newrob = max(rob1 + num, rob2)
        rob1 = rob2
        rob2 = newrob
    return rob2
    
def rob(self, nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return nums[0]
    else:
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))
```
