w = int(input('give weight:'))

if w <= 3:
    v = 3
elif w > 2 and w <= 5:
    v = 3 + (w-2)*2
else:
    v = 9 + (w-5)*3
print (v)
