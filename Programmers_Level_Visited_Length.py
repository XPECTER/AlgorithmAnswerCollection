def solution(dirs):
    dir_dic = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}
    pos = [0, 0]
    path = set()

    for i in list(dirs):
        dx, dy = dir_dic[i]
        if -6 < pos[0]+dx < 6 and -6 < pos[1]+dy < 6:
            if (pos[0], pos[1], pos[0]+dx, pos[1]+dy) not in path and (pos[0]+dx, pos[1]+dy, pos[0], pos[1]) not in path:
                path.add((pos[0], pos[1], pos[0]+dx, pos[1]+dy))

            pos[0] += dx
            pos[1] += dy

    return len(path)


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
