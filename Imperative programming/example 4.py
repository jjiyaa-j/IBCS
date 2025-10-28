n = int(input ('please give n:'))
if n <= 0:
    print ('not a positive')
else:
    result = 1
    for d in range(2,n+1): #use the for statement when you know the amount of variable in the sequence or whatever it is
        result *= d

    print (result)
