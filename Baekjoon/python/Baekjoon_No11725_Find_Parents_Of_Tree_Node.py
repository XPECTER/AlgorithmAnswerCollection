from collections import defaultdict
import sys
# Runtime error : recursion error 백준에선 1000이 끝이기 때문에,,,
# sys.setrecursionlimit(10**6)

N = int(input())
answer = [0] * N
dic = defaultdict(list)

for _ in range(N - 1):
    i, j = map(int, sys.stdin.readline().split())
    dic[i].append(j)
    dic[j].append(i)

# while로 푸는것도 괜찮을지도
def dfs(node: int, parents: int) -> None:
    answer[node - 1] = parents

    for i in dic[node]:
        if i != parents:
            dfs(i, node)

    return

dfs(1, 0)

print('\n'.join(map(str, answer[1:])))
