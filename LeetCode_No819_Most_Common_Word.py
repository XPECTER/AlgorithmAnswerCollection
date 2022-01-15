import re
from collections import Counter

def Solution(string : str, banned : list):
    words = [word for word in re.sub("[^\w]", ' ', string).lower().split() if word not in banned]
    answer = Counter(words)
    return answer.most_common(1)[0][0]


input = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(Solution(input, banned))