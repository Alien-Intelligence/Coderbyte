def SecondGreatLow(arr):
    li = arr[1:-1].split(',')
    lis = []
    for i in li:
        lis.append(int(i))
    sol = sorted (lis)

    if len(sol) == 2:
        mi2 = sol[1]
        ma2 = sol[0]

    elif len(sol) == 3:
        if sol[0] == sol[1] and sol[1]==sol[2]:
            mi2 = ma2 = sol[0]
        else:
            ha = sorted(list(set(sol)))
            mi2 = ha[1]
            ma2 = ha[-2]


    elif len(sol) > 3:
        ho = sorted (list(set(sol)))
        mi2 = ho[1]
        ma2 = ho[-2]
    print (sol)
    return str(mi2)+" "+str(ma2)
    # code goes here


# keep this function call here
print (SecondGreatLow(input()))





