def date_of_birth(ssn):
    d = int(ssn[0:2]) #the output has the be an integer tuple not the strings written so need to add the int in order to convert into interger
    m = int(ssn[2:4])
    c = ssn[6]
    if c == '+':
        y = int('18' + ssn[4:6])
    elif c == 'A':
       y = int('20'+ ssn[4:6])
    else:
        y =  int('19' + ssn[4:6])
    return (y,m,d)

print (date_of_birth('140598+abcd'))


