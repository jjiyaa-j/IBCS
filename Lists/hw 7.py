lst = []
while (a := int(input('give integers: '))) > 0:
    if a not in lst:
        lst.insert (0,a)
    else:
        lst.remove (a)
        lst.insert (0,a)
       
print (lst)



