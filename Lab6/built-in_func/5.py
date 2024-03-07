def check_all_true(t):
    return all(t)

# Test the function
t1 = (1, 1, 1)
t2 = (True, False,True)
t3 = (True, True)
t4 = ()

print(check_all_true(t1))  
print(check_all_true(t2))  
print(check_all_true(t3))
print(check_all_true(t4))   