#1
lst = []
for i in range (8):
    lst.append (i**2)
print (lst)
print ()
#2
lst = []
for i in range (4):
    lst.append (f'2**{i} is {2**i}')
print (lst)
print ()

#3
lst = []
lst_f = []

for i in range (5,11):
    lst.append (i)
for i  in enumerate (lst):
    lst_f.append (i)
print(lst_f)
