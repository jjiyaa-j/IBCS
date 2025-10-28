v = 10
while v <= 37:
    print (v, end=' ')
    v += 3
print ()

v = 998
while v >= 900:
    print (v, end=' ')
    v -= 2
print ()

for v in range (1,21):
    if v % 2 == 0:
        p = -1
    else:
        p = 1
    print (p, end=' ')
print ()

for v in range (1,61):
    if v % 3 == 0:
        p = 9
    else:
        p = 7
    print (p, end=' ')
print ()
