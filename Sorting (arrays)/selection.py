def selection_sort (array): 
    for i in range (len(array) - 1): #0,1,...., n-2
        min_value = array[i]
        min_index = i
        for j in range (i + 1, len(array)):
            if array[j] < min_value:
                min_value = array[j]
                min_index = j
        if min_index != i:
            #swap values
            array[min_index] = array[i]
            array[i] = min_value

array = [47,8,9,3,6]
selection_sort(array)
print(array)


def time_sort(algo, n):
    import time, random

    # n samples with replacement from [0,1,...,n-1]
    data = random.choices(range(n), k=n)

    start = time.process_time()
    algo(data)
    end = time.process_time()
    return end - start

