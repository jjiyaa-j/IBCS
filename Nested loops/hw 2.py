a = [1,2,3,4,5]
b = [6,7,8,9,10,4]

flag = False
for n in range(len(a)):
    for m in range (len(b)):
        if a[n] == b[m]:
            flag = True

print (flag)
