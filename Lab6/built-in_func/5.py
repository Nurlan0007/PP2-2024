def check_all_true(t):
    return all(t)

# Test the function
t1 = (True, True, True)
t2 = (True, False, True)
t3 = ()

print(check_all_true(t1))  
print(check_all_true(t2))  
print(check_all_true(t3))  