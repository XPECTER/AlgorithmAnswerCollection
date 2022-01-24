import sys

N = int(input())
a_map = []
stack = []
answer = []
cnt = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(N):
    a_map.append(list(sys.stdin.readline().rstrip('\n')))

for i in range(N):
    for j in range(N):
        if a_map[i][j] == '1':
            stack.append((i, j))

            while stack:
                x, y = stack.pop()

                if a_map[x][y] == '0':
                    continue

                a_map[x][y] = '0'
                cnt += 1

                for k in range(4):
                    nX = x + dx[k]
                    nY = y + dy[k]

                    if 0 <= nX < N and 0 <= nY < N and a_map[nX][nY] == '1':
                        stack.append((nX, nY))

            answer.append(cnt)
            cnt = 0

print(len(answer))
for e in sorted(answer):
    print(e)
