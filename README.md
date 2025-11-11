# Python learning and projects
Repository where I will save my Python learning progress by following different courses and creating projects.

## Courses
- [Data Analysis with Python](https://www.freecodecamp.org/learn/data-analysis-with-python/) `in-progress`
- [Scientific Computing with Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/das) `in-queue`
 
## Projects / Challenges
- Blood on The Clocktower Storyteller AI `in-progress`
- Volleyball Stats Tracker `in-progress`
- Gantt Chart
- Password Locker
- Table Printer
- Scripts to make my life at job easier

```
from math import comb
from collections import Counter

def search_pascal_multiples_fast(row_limit):
    # Implement your fast function here. Feel free to copy-paste and then change the slow function from below, or to completely re-implement the function from scratch. 
    counts = Counter()
    # 120 is the first number to appear >3 times. It appears in row 10.
    # row 10: [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]
    # middle value for even rows: row_number / 2
    # odd rows have 2 middle values: round(row_number / 2) AND round(row_number / 2)+1
    # rows are symmetrial, so I dont need to check the same number multiple times
    
    
    '''
    # rows n=2..row_limit; interior positions are k=1..n-1, but exclude k=0 and k=n
    for n in range(2, row_limit + 1):
        half = n // 2
        for k in range(1, half + 1):
            val = comb(n, k)
            if 2 * k == n:
                counts[val] += 1    # middle term counted once
            else:
                counts[val] += 2    # symmetric pair k and n-k
    # strictly more than 3 occurrences
    return sorted(x for x, c in counts.items() if c > 3)
    '''
```
