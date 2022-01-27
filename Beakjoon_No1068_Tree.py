from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
tree = defaultdict(list)

idx = 0
lst = list(map(int, sys.stdin.readline().split()))
for i in lst:
    tree[i].append(idx)
    idx += 1

for i in range(N):
    if len(tree[i]) == 0:
        tree[i] = []

root = tree[-1][0]
print(tree)
erase_node_num = int(sys.stdin.readline())

def tree_cut(node_num):
    if tree[node_num] == 0:
        del tree[node_num]
        return

    for i in tree[node_num]:
        tree_cut(i)

    del tree[node_num]
    return

queue = deque([root])
while queue:
    node = queue.popleft()

    if erase_node_num in tree[node]:
        tree[node].remove(erase_node_num)
        break
    else:
        for i in tree[node]:
            queue.append(i)

tree_cut(erase_node_num)
answer = 0
for i in tree.keys():
    if len(tree[i]) == 0:
        answer += 1

print(tree)
print(answer)
