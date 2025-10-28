import random
n = 10
list_of_lists = [random.sample(list(range(n)),n) for i in range(5)]

print (list_of_lists)

lst = []

for i in list_of_lists:
    lst.extend (i)

print (lst) 
