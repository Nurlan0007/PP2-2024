def count_case(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

s = "Hello, World!"
upper, lower = count_case(s)
print(f"Number of uppercase letters: {upper}")
print(f"Number of lowercase letters: {lower}")