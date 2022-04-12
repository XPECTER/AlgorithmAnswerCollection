# 문제 : 신입사원 무지는 게시판 불량 이용자를 신고하고 처리 결과를 메일로 발송하는 시스템을 개발하려 합니다. 무지가 개발하려는 시스템은 다음과 같습니다.
# 각 유저는 한 번에 한 명의 유저를 신고할 수 있습니다.
# 신고 횟수에 제한은 없습니다. 서로 다른 유저를 계속해서 신고할 수 있습니다.
# 한 유저를 여러 번 신고할 수도 있지만, 동일한 유저에 대한 신고 횟수는 1회로 처리됩니다.
# k번 이상 신고된 유저는 게시판 이용이 정지되며, 해당 유저를 신고한 모든 유저에게 정지 사실을 메일로 발송합니다.
# 유저가 신고한 모든 내용을 취합하여 마지막에 한꺼번에 게시판 이용 정지를 시키면서 정지 메일을 발송합니다.

from collections import defaultdict, Counter


def solution(id_list, report, k):
    answer = {id : 0 for id in id_list}     # 누가 결과를 받을 지 저장

    dic = defaultdict(list)                 # 신고한 사람이 누굴 신고했는지 저장 -> 신고받은 사람을 저장하는게 낫다
    dic_count = defaultdict(int)            # dic을 신고받은 사람으로 바꾸면 len()으로 해결할 수 있다

    report = list(set(report))              # 한 사람이 같은 사람을 여러번 신고해도 1번으로 취급한다.
    for re in report:
        print(re)
        re = re.split(" ")

        if re[1] not in dic[re[0]]:
            dic[re[0]].append(re[1])
            dic_count[re[1]] += 1

    for key, val in dic_count.items():
        if val >= k:
            for id in id_list:
                if key in dic[id]:
                    answer[id] += 1

    print(dic)
    print(dic_count)
    return list(answer.values())


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))