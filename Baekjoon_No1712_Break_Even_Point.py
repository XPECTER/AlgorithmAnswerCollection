A, B, C = map(int, input().split())
if C - B <= 0:
    print(-1)
else:
    print(int(A / (C - B)) + 1)

# A는 고정비, B는 가변비용, C는 제품 비용
# A + Bn <= Cn 이 되는 지점
# A <= Cn - Bn
# A <= (C - B)n
# n <= A / (C - B)