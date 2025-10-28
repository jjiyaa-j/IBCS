#same thing as key-value mapping but with objects instead
class Reservation:
    def __init__(self,name,room):
        self.name = name
        self.room = room

reservations = [Reservation('Ville',101), Reservation('Maija',103)]

def seq_search_object(name,reservations):
    index = 0
   
    while index < len(reservations):
        r = reservations[index] #give it a variable so that you dont need to repeat such a long expression twice and you cna just write r. and then whatever you want 
        if r.name == name:
            return r.room
        index += 1

    return -1

print (seq_search_object('Maija', reservations))
print (seq_search_object('Farid', reservations))