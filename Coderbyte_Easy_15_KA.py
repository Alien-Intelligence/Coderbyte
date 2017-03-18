def Palindrome(st):
    s = "".join(st.split())
    if s == s[::-1]:
        return "true"
    else:
        return "false"
        # code goes here

# keep this function call here
print (Palindrome(input()))
