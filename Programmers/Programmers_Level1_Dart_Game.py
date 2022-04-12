import re


def solution(dartResult: str) -> int:
    dartResult = re.split('(\d+)([SDT])([*#]?)', dartResult)
    answer = []
    score = 0
    print(dartResult)

    for strs in dartResult:
        if strs.isdigit():
            score = int(strs)
            continue

        if 'D' in strs:
            score **= 2
        elif 'T' in strs:
            score **= 3

        if '*' in strs:
            score *= 2
            answer[-1] *= 2
        elif '#' in strs:
            score *= -1

        answer.append(score)
        score = 0

    return sum(answer)


if __name__ == "__main__":
    # assert solution("1T2D3D#") == -4
    # assert solution("1D2S3T*") == 59
    assert solution("1D2S#10S") == 9

