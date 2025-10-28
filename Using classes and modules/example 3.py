
def find_all(s,sub):
    result = []
    start = 0 #starting index of next find
    while start < len(s) and ( i := s.find(sub,start)) >= 0:
        result.append(i)
        start = i + 1

    return result

string = 'abababa'
sub = 'b'

print(find_all(string,sub))
