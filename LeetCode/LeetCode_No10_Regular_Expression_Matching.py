class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        s_idx = 0
        p_idx = 0

        while s_idx < s_len and p_idx < p_len:
            if p[p_idx].isalpha():
                if (p_idx + 1) == p_len:
                    if p[p_idx] != s[s_idx]:
                        return False
                    else:
                        break
                else:
                    if p[p_idx + 1] == '*':
                        while True:
                            if s[s_idx] == p[p_idx]:
                                s_idx += 1

                                if s_idx == s_len:
                                    return True
                            else:
                                break
                        p_idx += 2
                    else:
                        if p[p_idx] == s[s_idx]:
                            p_idx += 1
                            s_idx += 1
                            continue
                        else:
                            return False
            elif p[p_idx] == '.':
                if p_idx + 1 != p_len:
                    if p[p_idx + 1] == '*':
                        re = s[s_idx]
                        while s[s_idx] == re:
                            s_idx += 1
                    else:
                        p_idx += 1
                        s_idx += 1

        return True


a = Solution()
print(a.isMatch('aab', 'c*a*b'))
print(a.isMatch('aa', 'a'))
print(a.isMatch('aa', 'a*'))