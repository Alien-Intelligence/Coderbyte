def TimeConvert(num):
    li = []
    li.append(str(int(num / 60)))
    li.append(":")
    li.append(str(num % 60))
    sol = "".join(li)
    return sol


# keep this function call here
print (TimeConvert(int(input())))