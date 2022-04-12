# 문제 : 자연수 n이 주어질 때 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return하세요

def solution(n):
    if n % 2:  # 홀수면 2가 답
        return 2
    else:  # 짝수면
        a = 2
        while a < n // 2:
            if n % a == 1:
                return a
            else:
                a += 1      # 그냥 a를 1씩 증가시키면서 나눠보는 건데.. 좀 맘에 안듦

        return n - 1        # 절반까지 나눠봐도 없으면 자신-1 이 답

print(solution(10)) # result = 3
print(solution(12)) # result = 11