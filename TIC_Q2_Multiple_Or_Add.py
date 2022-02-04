def Solution(strs: str) -> int:
    total = 0

    for i in range(len(strs)):
        num = int(strs[i])
        if total == 0 or num <= 1:
            total += num
        else:
            total *= num

    return total


print(Solution('567'))
print(Solution('02984'))
print(Solution('11111'))
print(Solution(''))
