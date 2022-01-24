# time : 68 ms

from itertools import combinations, product
import sys

L, C = map(int, sys.stdin.readline().split())
v = {'a', 'e', 'i', 'o', 'u'}   # 필터. 입력받은 문자가 모음이면 모음 List로 들어간다. 5개밖에 안되서 list를 써도 될듯?
con = []        # 자음 List
vow = []        # 모음 List
answer = []     # 완성된 암호 List

for c in sys.stdin.readline().split():
    if c in v:
        vow.append(c)
    else:
        con.append(c)

cnt = 1
while cnt <= len(vow) and L - cnt >= 2:
    ex_c = list(map("".join, list(combinations(con, L - cnt))))
    ex_v = list(map("".join, list(combinations(vow, cnt))))
    answer.extend(list(map("".join, list(product(ex_v, ex_c)))))
    cnt += 1

for word in sorted(list(map("".join, (map(sorted, answer))))):
    print(word)