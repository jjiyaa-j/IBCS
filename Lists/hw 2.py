list_p = []
list_n = []

while (a := int(input('give intergers:'))):
    if a > 0:
        list_p.append (a)
    elif a < 0:
        list_n.append (a)

if a == 0:
    print (list_p, list_n)

