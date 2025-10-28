def file_type(s):
    a = s.rfind('.', 1)
    return s[a+1:]

s = 'foo.doc'
print (file_type(s))
