def seq_search(key,array):
    index = 0
    found = False #can take away the found completely which simplifies the program so take away all found

    while not found and index < len(array): #take away the not found from this line too 
        if array[index] == key:
            found = True #the becomes "return True"
        index += 1

    return found #return False

array = [-2,9,11,12,13,14,15,22,142]
print (seq_search(15,array))

#binary 
def bin_search (key,array):
    lo = 0
    hi = len(array) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        val = array[mid]
        print (val)
        if val == key:
            return True
        elif val > key:
            hi = mid - 1
        else:
            lo = mid + 1
    
    return False
array = [-2,9,11,12,13,14,15,22,142]
print (bin_search(15,array))
