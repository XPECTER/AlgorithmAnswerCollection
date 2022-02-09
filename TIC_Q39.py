import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# case
for _ in range(int(input())):
    mars_matrix = []
    width = int(input())

    for _ in range(width):
        mars_matrix.append(list(map(int, input().split())))

    dist = [[INF] * width for _ in range(width)]
    q = [(mars_matrix[0][0], 0, 0)]
    dist[0][0] = mars_matrix[0][0]

    while q:
        energy, posX, posY = heapq.heappop(q)

        if energy > dist[posX][posY]:
            continue

        for i in range(4):
            nX, nY = posX + dx[i], posY + dy[i]

            if 0 <= nX < width and 0 <= nY < width:
                cost = energy + mars_matrix[nX][nY]

                if cost < dist[nX][nY]:
                    dist[nX][nY] = cost
                    heapq.heappush(q, (cost, nX, nY))

    print(dist[width - 1][width - 1])
