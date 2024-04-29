# fibonacci recursive function
fibonacci = lambda x : x if x <= 1 else fibonacci(x-1) + fibonacci(x-2)
print(fibonacci(int(input())))

# fibonacci for
# n = int(input())
# f = [0, 1]
# for i in range(2, n+1):
#     f.append(f[i-2] + f[i-1])
#
# print(f[n])