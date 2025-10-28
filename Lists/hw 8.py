lst = []
lst2 = []
while (a := input('give words: ')) != '!':
    lst.append (a)

while (b := int(input('give indices: '))) >= 0:
    lst2.append (b)

lst3 = [word for i, word in enumerate(lst) if i not in lst2]

print ('original:', lst)
print ('indices:', lst2)
print ('result:', lst3)
