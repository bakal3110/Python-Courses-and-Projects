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
def search_pascal_multiples_fast(row_limit):

    counts = Counter()

    # Building up Pascal's triangle with a dict of lists
    p_rows = [[factorial(n) // (factorial(k) * factorial(n - k)) for k in range(n+1)] for n in range(10, row_limit)]

    for i in range(len(p_rows)):
        row_length = round(len(p_rows[i]) / 2)
        if i % 2 == 0:
            counts[p_rows[i][row_length-1]] += 1
            for j in range(2, row_length-1): counts[p_rows[i][j]] += 2
        else:
            for j in range(2, row_length): counts[p_rows[i][j]] += 2

    
    numbers = [n for n, c in counts.items() if c > 3]

    return sorted(numbers)
```
