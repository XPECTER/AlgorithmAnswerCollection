import sys


while True:
    strs = sys.stdin.readline().rstrip('\n')

    if strs == '.':
        break

    stack = []
    flag = True
    for char in strs:
        if char.isalpha() or char == " ":
            continue

        if char == "(" or char == "[":
            stack.append(char)
            continue
        elif char == ")":
            if stack and stack[-1] == "(":
                stack.pop()
                continue
            else:
                flag = False
                break
        elif char == "]":
            if stack and stack[-1] == "[":
                stack.pop()
                continue
            else:
                flag = False
                break

    print("yes") if flag and not stack else print("no")
