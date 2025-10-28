def remove():
    OUT = []
    while (ORIG := int(input('give positive integers: '))) > 0:
        while (x := int(input('give number'))):
         for i in ORIG:
            if i != x:
               OUT.append (i)
            else:
               OUT.insert (0)

    print (OUT)










