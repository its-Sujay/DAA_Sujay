def reverse_string(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

s = "pots&pans"
result = reverse_string(s)
print("The reverse of", s, "is:", result)
