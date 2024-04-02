def str_to_int(s):
    # Base case: if the string is empty, return 0
    if not s:
        return 0
    return str_to_int(s[:-1]) * 10 + int(s[-1])


s=input("Enter a number in string format : ")
result = str_to_int(s)
print("Integer representation of", s, "is:", result)
