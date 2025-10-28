s = 'foobar'
sub = 'ob'
def dashify_substring(s,sub):
    if sub in s:
        return s.replace(sub,f'-{sub}-',1)
    else:
        return s
    
print (dashify_substring(s,sub))