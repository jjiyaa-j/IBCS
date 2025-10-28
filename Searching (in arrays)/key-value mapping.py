#if there is key and values both and we use parallel arrays
#has the more simplified/neater version from the previous code (sequential search.py)


def seq_search_room(name,names,rooms):
    index = 0
   
    while index < len(names):
        if names[index] == name:
            return rooms[index]
        index += 1

    return -1

names = ['Ville','Maija']
rooms = [101,103]
print (seq_search_room('Ville',names,rooms))
print (seq_search_room('Farid',names,rooms))

