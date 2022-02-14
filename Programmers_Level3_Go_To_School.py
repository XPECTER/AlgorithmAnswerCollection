def solution(m, n, puddles):
    tile = [[0] * (m + 1) for _ in range(n + 1)]
    tile[0][1] = 1

    for p in puddles:
        tile[p[0]][p[1]] = -1

    print(tile)

    for y in range(1, m + 1):
        for x in range(1, n + 1):
            print(x, y)
            if tile[x][y] == -1:
                continue
            if tile[x - 1][y] == -1 or tile[x][y - 1] == -1:
                tile[x][y] = max(tile[x - 1][y], tile[x][y - 1])
            else:
                tile[x][y] = (tile[x - 1][y] + tile[x][y - 1]) % 1000000007

    return tile[-1][-1]


print(solution(4, 3, [[2, 2]]))