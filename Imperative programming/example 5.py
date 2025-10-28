v = 9
while v <= 65:
    print (v, end=' ')
    v += 4
print () #so that the next example starts on a new line

d = 3
for x in range (13): 
    print (d, end= ' ')
    d *= 2
print ()

for v in range (1,41):
    if v % 4 == 0: # the % sign is when the remainder whne divided by a number in this case when the number divided by 4 gives the remainder 0
        x = -1
    else:
        x = v
    print (x, end=' ')
