def VowelCount(st):
    coun = []
    li = list(st)
    for i in li:
        if i in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            coun.append("NO")
    st = coun.count("NO")
    # code goes here
    return st


# keep this function call here
print (VowelCount(input()))