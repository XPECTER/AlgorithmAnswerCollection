def solution(dirs):
    dir_dic = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}
    x, y = 0, 0
    path = set()

    for i in list(dirs):
        nx, ny = x + dir_dic[i][0], y + dir_dic[i][1]
        if -6 < nx < 6 and -6 < ny < 6:
            path.add((x, y, nx, ny))
            path.add((nx, ny, x, y))
            x, y = nx, ny
    return len(path) // 2


    for i in list(dirs):
        nx, ny = x + dir_dic[i][0], y + dir_dic[i][1]
        if -6 < nx < 6 and -6 < ny < 6:
            if (x, y, nx, ny) not in path or (nx, ny, x, y) not in path:
                path.add((x, y, nx, ny))
            x, y = nx, ny

    return len(path)


assert(solution("ULURRDLLU")) == 7
assert(solution("LULLLLLLU")) == 7
