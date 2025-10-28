def read_ints():
    lst = []
    while (a := input('give intergers: ')) != '':
        lst.append(int(a))
    return lst

print (read_ints())

        