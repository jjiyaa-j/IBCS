#my solution did not account for negative numbers thus it was correct but not completely correct. 
#New solution
while (inp := input(('Enter a calcuation: '))) != '':
    [a_str, op, b_str] = inp.split()
    a_str, b_str = float(a_str), float(b_str)

    if (op == '+'):
        res = a_str + b_str

    elif (op == '-'):
        res = a_str - b_str

    elif (op == '*'):
        res = a_str * b_str
    
    else:
        print('FAILURE; RETRY.')
        continue


    print(res) #also does not account for negative numbers....