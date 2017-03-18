def LetterCapitalize(st):
    li = list(st.split())
    so = []
    for i in li:
        so.append(i[0].upper() + i[1:])

    sol = " ".join(so)

    # code goes here
    return sol


# keep this function call here
print (LetterCapitalize(input()))

