# Runtime: 40 ms, faster than 91.40% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 15.7 MB, less than 21.38% of Python3 online submissions for Valid Palindrome.
import re


def isPalindrome(s : str):
    s = s.lower()
    # s = s.upper()

    s = re.sub('[^a-z0-9]', '', s)
    print(s)
    return True if s == s[::-1] else False


# Runtime: 48 ms, faster than 71.32% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 14.4 MB, less than 93.52% of Python3 online submissions for Valid Palindrome.
def isPalindrome2(s : str):
    s = s.lower()
    i, j = 0, len(s)-1

    while i < j:
        while i < j and s[i].isalnum() == False:
            i += 1
        while i < j and s[j].isalnum() == False:
            j -= 1

        if i >= j:
            break
        else:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

    return True


# __name__ == "__main__" 을 쓰는 이유는
# 이 페이지를 인터프리터로 실행하면 아래를 main을 실행하고,
# 이 페이지를 import해서 실행하면 아래를 실행하지 않는다.
if __name__ == "__main__":
    print(isPalindrome2("A man, a plan, a canal: Panama"))
    print(isPalindrome2("race a car"))
