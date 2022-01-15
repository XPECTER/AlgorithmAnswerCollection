def Solution(l: list):
    dig, let = [], []

    for e in l:
        if e.split()[1].isdigit():
            dig.append(e)
        else:
            let.append(e)

    let.sort(key= lambda x : (x.split()[1:], x.split()[0]))
    return let + dig


logs = ["dig1 8 1 5 1", "let1 art can" , "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(Solution(logs))