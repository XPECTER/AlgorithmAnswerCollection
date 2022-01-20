import re


def solution(new_id):
    answer = new_id.lower()
    answer = re.sub('[^0-9a-z-_.]', '', answer)
    answer = re.sub('\.+', '.', answer).strip('.')
    answer = 'a' if len(answer) == 0 else answer[:15].rstrip('.')
    return answer if len(answer) > 2 else answer + "".join(answer[-1] for _ in range(3 - len(answer)))


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
