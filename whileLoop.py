# i = 1
# while i <= 5:
#     print(i)
#     i += 1

n = 5
factorial = 1
i = 1
if n == 0:
    factorial = 1
else:
    while i <= n:
        factorial *= i
        i += 1
print(factorial)    
