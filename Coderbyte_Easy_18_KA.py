def LetterCountI(st):
    li = st.split()

    def check(s):
        ma = 0
        for i in str(s):
            if s.count(i) > ma:
                ma = s.count(i)
        return ma

    sol = []
    for j in li:
        sol.append(check(j))

    if sol.count(1) == len(sol):
        return "-1"
    else:
        for k in range(0, len(sol)):
            if sol[k] == max(sol):
                key = k
                break


                # code goes here
        return li[k]


# keep this function call here
print (LetterCountI(input()))



