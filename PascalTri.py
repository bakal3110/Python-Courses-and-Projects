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
