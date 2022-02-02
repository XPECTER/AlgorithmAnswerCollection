import collections
import heapq

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # used sorted. time : 66ms
        # return sorted(s) == sorted(t)

        # used Counter. time : 61ms
        # s_cnt = collections.Counter(s)
        # t_cnt = collections.Counter(t)
        # return True if s_cnt == t_cnt else False

        # used heap. time : 107ms
        s_lst, t_lst = list(s), list(t)
        heapq.heapify(s_lst)
        heapq.heapify(t_lst)
        for i in range(min(len(s_lst), len(t_lst))):
            char_s = heapq.heappop(s_lst)
            char_t = heapq.heappop(t_lst)
            if char_s != char_t:
                return False

        return False if len(s_lst) >= 1 or len(t_lst) >= 1 else True


print(Solution().isAnagram("anagram", "nagaram"))
print(Solution().isAnagram("a", "ab"))