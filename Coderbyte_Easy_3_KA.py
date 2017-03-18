def LongestWord(sen):
    a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
    A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    li = sen.split()
    nl = []
    for i in li:
        new = ""
        for j in i:
            if j in a or j in A or j in s:
                new = new + j
        nl.append(new)

    sol = nl[0]

    for k in range(1, len(nl)):
        if len(nl[k]) > len(sol):
            sol = nl[k]

    return sol



    # code goes here


# keep this function call here
print (LongestWord(input()))
