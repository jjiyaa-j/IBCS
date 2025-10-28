highest = 0
h = 0
for t in range (1,101):
    x = t*(t - 20) * (t - 100) + 120000
    p = (t-1) * ((t-1) - 20) * ((t-1) - 100) + 120000
    if t == 1:
        highest = p - x
    elif highest < (p - x):
        highest = p - x
        h = t
print (h)



    