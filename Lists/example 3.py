words = ['hello', 'ei', 'moi', 'inte', 'aloha', 'penguin']

#another way of doing it:
# i = 0 #with a while-loop
# while (i < len(words)):
#     if len(words[i]) <= 4:
#         words.pop(i)
#     else:
#         i += 1

# print (words)

words = [w for w in words if len(w) > 4] #with list comprehension
print (words)


