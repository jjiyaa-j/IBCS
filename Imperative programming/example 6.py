low = 0
high = 0
for n in range(51): #from 0 - 50 so that's why range is 51
    val = n*(n-30)*(n-50) #value is this equation
    if val > high:
        high = val
    if val < low:
        low = val
print (low,high)
