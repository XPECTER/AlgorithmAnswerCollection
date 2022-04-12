import re


def solution(files):
    # 테스트 1 〉	통과 (0.17ms, 10.6MB)
    # 테스트 2 〉	통과 (0.18ms, 10.5MB)
    # 테스트 3 〉	통과 (29.71ms, 10.6MB)
    # 테스트 4 〉	통과 (28.24ms, 10.6MB)
    # 테스트 5 〉	통과 (28.93ms, 10.6MB)
    # 테스트 6 〉	통과 (24.79ms, 10.6MB)
    # 테스트 7 〉	통과 (24.79ms, 10.6MB)
    # 테스트 8 〉	통과 (21.43ms, 10.6MB)
    # 테스트 9 〉	통과 (35.56ms, 10.6MB)
    # 테스트 10 〉	통과 (22.96ms, 10.6MB)
    # 테스트 11 〉	통과 (22.92ms, 10.6MB)
    # 테스트 12 〉	통과 (39.22ms, 10.7MB)
    # 테스트 13 〉	통과 (17.73ms, 10.7MB)
    # 테스트 14 〉	통과 (99.58ms, 10.7MB)
    # 테스트 15 〉	통과 (95.45ms, 10.8MB)
    # 테스트 16 〉	통과 (24.02ms, 10.7MB)
    # 테스트 17 〉	통과 (13.51ms, 10.6MB)
    # 테스트 18 〉	통과 (15.18ms, 10.6MB)
    # 테스트 19 〉	통과 (19.04ms, 10.7MB)
    # 테스트 20 〉	통과 (17.49ms, 10.7MB)
    def merge(l_list: list, r_list: list) -> list:
        result = []
        i = j = 0

        while i < len(l_list) and j < len(r_list):
            left_file = re.split('([a-zA-Z-. ]+)(\d+)', l_list[i])
            right_file = re.split('([a-zA-Z-. ]+)(\d+)', r_list[j])

            left_head = left_file[1].lower()
            right_head = right_file[1].lower()
            left_num = int(left_file[2])
            right_num = int(right_file[2])

            if left_head == right_head:
                if left_num == right_num or left_num < right_num:
                    result.append(l_list[i])
                    i += 1
                else:
                    result.append(r_list[j])
                    j += 1
            else:
                temp = sorted([left_head, right_head])
                if temp[0] == left_head:
                    result.append(l_list[i])
                    i += 1
                else:
                    result.append(r_list[j])
                    j += 1

        if i < len(l_list):
            result.extend(l_list[i:])

        if j < len(r_list):
            result.extend(r_list[j:])

        return result

    def merge_sort(lst: list) -> list:
        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2
        return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))

    return merge_sort(files)

    # 테스트 1 〉	통과 (0.09ms, 10.4MB)
    # 테스트 2 〉	통과 (0.12ms, 10.4MB)
    # 테스트 3 〉	통과 (2.67ms, 10.6MB)
    # 테스트 4 〉	통과 (2.70ms, 10.7MB)
    # 테스트 5 〉	통과 (2.66ms, 10.7MB)
    # 테스트 6 〉	통과 (2.45ms, 10.6MB)
    # 테스트 7 〉	통과 (2.48ms, 10.6MB)
    # 테스트 8 〉	통과 (2.20ms, 10.6MB)
    # 테스트 9 〉	통과 (2.30ms, 10.6MB)
    # 테스트 10 〉	통과 (2.37ms, 10.6MB)
    # 테스트 11 〉	통과 (2.33ms, 10.6MB)
    # 테스트 12 〉	통과 (2.60ms, 10.6MB)
    # 테스트 13 〉	통과 (2.54ms, 10.7MB)
    # 테스트 14 〉	통과 (3.48ms, 10.7MB)
    # 테스트 15 〉	통과 (3.57ms, 10.7MB)
    # 테스트 16 〉	통과 (2.36ms, 10.6MB)
    # 테스트 17 〉	통과 (2.86ms, 10.6MB)
    # 테스트 18 〉	통과 (2.25ms, 10.6MB)
    # 테스트 19 〉	통과 (2.63ms, 10.6MB)
    # 테스트 20 〉	통과 (2.60ms, 10.6MB)
    a = sorted(files, key=lambda file: int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file: re.split('\d+', file.lower())[0])

    return b

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(["muzi1.txt", "MUZI1.txt", "muzi001.txt", "muzi1.TXT"]))
print(solution(["MuZi.00001", "m.UzI00010"]))