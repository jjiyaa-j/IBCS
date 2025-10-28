lst = []

while (i := input('give words: ')) != '!':
    lst.append (i)


while (b := input('give more words: ')) != '!':
    for i in lst:
        if i == b:
            print ('hit')

