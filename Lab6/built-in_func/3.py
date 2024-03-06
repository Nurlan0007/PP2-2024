def is_polindrome(s):
    return s == s[::-1]

s = "kazak"
print(f"{is_polindrome(s)}")