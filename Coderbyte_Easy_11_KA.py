def ABCheck(st):
    if (st.find('a') == -1 and st.find('A') == -1) or (st.find('b') == -1 and st.find('B') == -1):
        return "false"

    sol = ""
    li = list(st)

    for j in range(0, 3):
        if li[j] == 'a':
            if li[(j + 3)<len(li)] == 'b' or li[(j - 3)>=0] == 'b':
                sol = "true"
            else:
                sol = "false"


    for i in range(3, len(li)-3):
        if li[i] == 'a':
            if li[i + 3] == 'b' or li[i - 3] == 'b':
                sol = "true"
            else:
                sol = "false"

    return sol


# keep this function call here
print (ABCheck(input()))




