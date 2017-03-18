def SimpleAdding(a):
    sol = 0

    for i in range(1, a + 1):
        sol = sol + i

    return sol


# keep this function call here
print(SimpleAdding(int(input())))
