#write a function seq_search(key,array) questionn fromm the handout
def seq_search(key,array):
    index = 0
    found = False #can take away the found completely which simplifies the program so take away all found

    while not found and index < len(array): #take away the not found from this line too 
        if array[index] == key:
            found = True #the becomes "return True"
        index += 1

    return found #return False

array = [-2,9,11,12,39,48]
print (seq_search(11,array))
print (seq_search(13, array))

#time search function to see how long the running time is)
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

