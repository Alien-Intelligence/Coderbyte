def ExOh(st):
    x = []
    o = []

    for i in list(st):
        if i == 'x':
            x.append('x')
        elif i == 'o':
            o.append('o')

    if x.count('x') == o.count('o'):
        return "true"
    else:
        return "false"


# keep this function call here
print (ExOh(input()))
