def last_dot_kept(s):
    dot = '.'
    count = s.count(dot)
    return s.replace(dot,'-dot-',count -1)

print (last_dot_kept('foo.bar.whatever'))

