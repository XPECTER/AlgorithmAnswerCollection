import re

def isPalindrome(s : str):
    s = s.lower()
    # s = s.upper()

    s = re.sub('[^a-z0-9]', '', s)
    print(s)
    return True if s == s[::-1] else False

# def isPalindrome2(s : str):
#     s = s.lower()
#
#     for i in range(len(str) / 2):
#         j = len(str) - 1 - i
#         if s[i] != s[j]:
#             return False
#
#     return True

if __name__ == "__main__":
    print(isPalindrome("A man, a plan, a canal: Panama"))
    print(isPalindrome("race a car"))
