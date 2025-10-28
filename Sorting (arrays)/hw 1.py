#1.1 selection sort
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
            print (array)

array = [-4,11,7,-12,6,1]
print (array) 
selection_sort(array)
print ()

#1.2 bubble sort
def bubble_sort (array1):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(array1) - 1):
            if array1[i] > array1[i + 1]:
                (array1[i], array1[i+1]) = (array1[i+1], array1[i])
                sorted = False
                print (array1)

array1 = [-4,11,7,-12,6,1]
bubble_sort(array1)