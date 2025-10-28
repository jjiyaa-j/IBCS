n = 0
found = False
while found == False:
    if (n**3-16)%47 == 0:
        found = True
    else:
        n += 1
print (n)


