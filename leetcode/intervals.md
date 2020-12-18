# Intervals

+ [Merge Intervals](#merge-intervals)
+ [Insert Interval](#insert-interval)
+ [Non-overlapping Intervals](#non-overlapping-intervals)

## Merge Intervals

https://leetcode.com/problems/merge-intervals/

``` python
def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: 
            return intervals 
        intervals.sort(key=lambda x: x[0]) 
        merged = [intervals[0]]
        for interval in intervals:
            last = merged[-1]
            if last[1] >= interval[0]:
                last[1] = max(interval[1], last[1])
            else:
                merged.append(interval)
        return merged
```

## Insert Interval

https://leetcode.com/problems/insert-interval/

```python
def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        intervals = sorted(intervals)
        while i < len(intervals) and intervals[i][0] < newInterval[0]:
            i += 1
        intervals.insert(i, newInterval)
        merge = []
        for i in intervals:
            if not merge or merge[-1][1] < i[0]:
                merge.append(i)
            else:
                merge[-1][1] = max(merge[-1][1], i[1])
        return merge
```

## Non-overlapping Intervals

https://leetcode.com/problems/non-overlapping-intervals

```python
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        num_remove = 0
        if not intervals:
            return num_remove
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][0]
        for interval in intervals:
            if interval[0] < end:
                num_remove += 1
            else:
                end = interval[1]
        return num_remove
```

