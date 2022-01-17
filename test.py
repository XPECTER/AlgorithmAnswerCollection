a = [1,2,3,4]

print(id(a))


b = [1,2,3,4]

# if a is b:
#     print(True)
# else:
#     print(False)
#
# if a == b:
#     print(True)
# else:
#     print(False)

print(id(a[0]), id(a[1]),id(a[2]) ,id(a[3]))

a[0] = [1,2,3]

print(id(a[0]), id(a[1]),id(a[2]) ,id(a[3]))

print(a)

a[0] = 1

print(id(a[0]), id(a[1]),id(a[2]) ,id(a[3]))

a[0] += 3

print(id(a[0]), id(a[1]),id(a[2]) ,id(a[3]))