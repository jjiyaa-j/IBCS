lst = []
lst2 = []

while not (a := int(input('give intergers: '))) < 0:
    lst.append (a)

for i in lst:
     if i not in lst2:
        lst2.append (i)

print (lst)
print (lst2)




