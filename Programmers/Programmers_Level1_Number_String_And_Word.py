def solution(s):
    num_string = ["zero", "one", 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for c, i in zip(num_string, num):
        s = s.replace(c, i)

    return int(s)


print(solution("one4seveneight"))       # 1478
print(solution("23four5six7"))          # 234567
print(solution("2three45sixseven"))     # 234567
print(solution("123"))                  # 123
