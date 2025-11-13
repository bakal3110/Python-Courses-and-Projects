from collections import Counter

def find_frequent_binomials_fast(min_n=10, max_n=250, threshold=3):
    freq = Counter()
    
    for n in range(min_n, max_n + 1):
        # Start with C(n, 2)
        current = n * (n - 1) // 2
        freq[current] += 1
        
        # Compute up to C(n, n-2) using recurrence
        for k in range(2, n - 2):
            current = current * (n - k) // (k + 1)
            freq[current] += 1
    
    # Single pass to collect and sort frequent values
    result = []
    for val, count in freq.items():
        if count > threshold:
            result.append(val)
    
    result.sort()
    return result

def find_frequent_binomials_ultra_fast(min_n=10, max_n=250, threshold=3):
    # Estimate maximum possible unique values
    max_unique = (max_n - min_n + 1) * (max_n - 3) // 2
    freq = {}
    
    for n in range(min_n, max_n + 1):
        current = n * (n - 1) // 2
        freq[current] = freq.get(current, 0) + 1
        
        for k in range(2, n - 2):
            current = current * (n - k) // (k + 1)
            freq[current] = freq.get(current, 0) + 1
    
    # Build result during single pass
    result = []
    for val, count in freq.items():
        if count > threshold:
            result.append(val)
    
    result.sort()
    return result

def find_frequent_binomials_fastest(min_n=10, max_n=250, threshold=3):
    freq = {}
    
    for n in range(min_n, max_n + 1):
        # Manual computation for small optimization
        current = n * (n - 1) // 2
        freq[current] = freq[current] + 1 if current in freq else 1
        
        k = 2
        while k < n - 2:
            current = current * (n - k) // (k + 1)
            freq[current] = freq[current] + 1 if current in freq else 1
            k += 1
    
    # Pre-allocate result array for speed
    result = []
    for val in freq:
        if freq[val] > threshold:
            result.append(val)
    
    result.sort()
    return result

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
    
def search_pascal_multiples_fast2(row_limit):

    counts = Counter()

    for n in range(10, row_limit + 1):
        # n is the row, row length is n
        half = n // 2
        for k in range(2, half+1):
            value = factorial(n) // (factorial(k) * factorial(n - k))
            if k % 2 == 0:
                if k*2 == n: counts[value] += 1
                else: counts[value] += 2
            else:
                counts[value] += 2

    
    numbers = [n for n, c in counts.items() if c > 3]

    return sorted(numbers)
    
def search_pascal_multiples_fast3(row_limit):

    counts = Counter()

    for n in range(10, row_limit + 1):
        # n is the row, row length is n
        half = n // 2
        for k in range(2, half+1):
            value = comb(n, k)
            if k % 2 == 0:
                if k*2 == n: counts[value] += 1
                else: counts[value] += 2
            else:
                counts[value] += 2

    
    numbers = [n for n, c in counts.items() if c > 3]

    return sorted(numbers)
    
def search_pascal_multiples_fast4(row_limit):

    counts = Counter()

    for n in range(10, row_limit + 1):
        half = n // 2
        for k in range(2, half + 1):
            value = comb(n, k)
            if 2 * k == n:
                counts[value] += 1    # middle term counted once
            else:
                counts[value] += 2    # symmetric pair k and n-k

    return sorted(n for n, c in counts.items() if c > 3)
    
def search_pascal_multiples_fast5(row_limit):
    freq = {}
    
    for n in range(10, row_limit + 1):
        # Manual computation for small optimization
        current = n * (n - 1) // 2
        freq[current] = freq[current] + 1 if current in freq else 1
        
        k = 2
        while k < n - 2:
            current = current * (n - k) // (k + 1)
            freq[current] = freq[current] + 1 if current in freq else 1
            k += 1
    
    # Pre-allocate result array for speed
    result = []
    for val in freq:
        if freq[val] > 3:
            result.append(val)
    
    result.sort()
    return result

import timeit

def benchmark():
    min_n, max_n, threshold = 10, 250, 3
    
    # Test all versions
    versions = [
        find_frequent_binomials_fast,
        find_frequent_binomials_ultra_fast,
        find_frequent_binomials_fastest
    ]
    
    for version in versions:
        time_taken = timeit.timeit(lambda: version(min_n, max_n, threshold), number=10)
        result = version(min_n, max_n, threshold)
        print(f"{version.__name__}: {time_taken:.4f}s, found {len(result)} values")

# benchmark()
