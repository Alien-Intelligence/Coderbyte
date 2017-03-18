def ArithGeo(arr):
    checkari = "true"
    firstari = arr[1] - arr[0]
    for i in range(0, len(arr)-1):
        if arr[i + 1] - arr[i] == firstari:
            checkari = "ture"
        else:
            checkari = "false"

    checkgeo = "true"
    firstgeo = int(arr[1] / arr[0])
    for j in range(0, len(arr)-1):
        if int([i + 1] / arr[i]) == firstgeo:
            checkgeo = "true"
        else:
            checkgeo = "false"
    if checkari == "true":
        return "Arithmetic"
    elif checkgeo == "true":
        return "Geomatric"
    else:
        return "-1"


# keep this function call here
print (ArithGeo(input()))