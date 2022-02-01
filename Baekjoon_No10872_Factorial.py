# factorial recursive function
factorial = lambda x : x * factorial(x-1) if x > 1 else 1
print(factorial(int(input())))

# factorial for
# result = 1
# for i in range(2, int(input()) + 1):
#     result *= i
# print(result)
