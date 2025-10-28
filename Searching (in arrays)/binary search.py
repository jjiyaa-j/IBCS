def bin_search (key,array):
    lo = 0
    hi = len(array) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        val = array[mid]
        if val == key:
            return True
        elif val > key:
            hi = mid - 1
        else:
            lo = mid + 1
    
    return False

#time swarch function added here too so that can figure out the running time of this logorithmic time complexity
def time_search(algo, n, /, sort_data=False):
    import random, time

    # n samples with replacement from [0,1,...,n-1]
    data = random.choices(range(n), k=n)
    if sort_data: data.sort()
    key = n # never found, ensures worst case

    start = time.process_time()
    algo(key, data)
    end = time.process_time()
    return end - start

array = [1,4,7,9,10,26,48]


