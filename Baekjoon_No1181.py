import sys

# lst = sys.stdin.readlines()[1:]
# lst = lst.split('\n')

n = int(sys.stdin.readline())
lst = set()

for _ in range(n):
    word = sys.stdin.readline().rstrip('\n')
    lst.add(word)

# lst.sort(key=lambda x: len(x))
lst = list(lst)
lst.sort()
lst.sort(key=len)

print(*lst, sep='\n')

# lst = sorted(lst, key=len)
# print(lst)