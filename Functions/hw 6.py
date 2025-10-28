lst = [1,2,3,4,5,6,7,8,9,10]
def alternate(lst):
    list_new = []
    while len(lst) > 0:
        f = lst.pop(0)
        list_new.append(f)

        if len(lst) > 0:
            g = lst.pop(-1)
            list_new.append(g)
    return list_new

print (alternate(lst))
