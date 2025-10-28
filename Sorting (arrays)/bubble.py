def bubble_sort (array):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                (array[i], array[i+1]) = (array[i+1], array[i])
                sorted = False
    return array

array = [7,9,11,2]
print (bubble_sort(array))