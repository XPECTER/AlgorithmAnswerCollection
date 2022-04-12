# 문제 : anagram 단어 묶기
# anagram은 문자 배열만 바꿔 다른 단어를 만드는 것을 말한다. ex) eat, aet, tea

from collections import defaultdict

def groupAnagrams(strs):
    dic = {}

    for word in strs:
        # word.sort -> 반환값 없음, word가 정렬되서 가지고 있던 값이 바뀜 'eat' -> ['a','e','t']
        # sorted(word) -> 정렬된 문자열을 반환, 원래 word는 바뀌지 않음
        key = "".join(sorted(word)) # 'eat' => ['a', 'e', 't'] => 'aet'
        if key not in dic.keys():
            dic[key] = [word]
        else:
            dic[key].append(word)

        # key가 있는지 없는지 신경 안쓰려면 defaultdict를 쓰면 된다.
        # dic = defaultdict(list)
        # dic[key].append(word)

    dic2 = defaultdict(list)

    for word in strs:
        dic2["".join(sorted(word))].append(word)

    print(list(dic.values()))
    print(list(dic2.values()))
    return


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
groupAnagrams(strs)