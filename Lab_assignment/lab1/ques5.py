def is_palindrome(s):

    if len(s) <= 1:
        return True
    
    #Recursively check the substring excluding the first and last characters
    if s[0] == s[-1]:#
        return is_palindrome(s[1:-1])
    else:
        return False

# Test the function
print(is_palindrome("mom"))  
print(is_palindrome("malayalam"))
print(is_palindrome("hello"))  
