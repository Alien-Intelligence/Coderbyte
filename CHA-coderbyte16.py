def ArithGeo(arr): 
    arith=[arr[i+1]-arr[i] for i in range(len(arr)-1)]
    geo=[float(arr[i+1])/float(arr[i]) for i in range(len(arr)-1)]
    if len(list(set(arith)))==1:
        return "Arithmetic"
    elif len(list(set(geo)))==1:
        return "Geometric"
    else:
        return -1
    
print ArithGeo(raw_input())  
















  
