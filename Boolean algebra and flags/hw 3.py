while ((s := int(input('give number: '))) <= 0):
    print ('invalid')
n = 1
found = False

while found == False: #to make a loop so if the condition does not fulfil it moves onto the next number until the condiiton applies
    if n**3 - 10*n**2 > s:
        found = True
    else:
        n += 1

print (n)


