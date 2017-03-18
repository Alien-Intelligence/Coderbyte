def CheckNums(num1,num2):

    if num1 == num2:
        print("-1")
    elif num1 < num2:
        print("true")
    elif num1 > num2:
        print("false")


CheckNums(int(input()),int(input()))
