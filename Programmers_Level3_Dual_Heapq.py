import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    length = 0

    for strs in operations:
        command, value = strs.split()

        if command == "I":
            heapq.heappush(max_heap, -int(value))
            heapq.heappush(min_heap, int(value))
            length += 1
        else:
            if length == 0:
                continue

            if int(value) == 1:
                heapq.heappop(max_heap)
                min_heap.pop()
            else:
                heapq.heappop(min_heap)
                max_heap.pop()
            length -= 1

    return [-max_heap[0], min_heap[0]] if length > 0 else [0, 0]


print(solution(["I 16", "D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))
print(solution(["I 4", "I 3", "I 2", "I 1", "D 1", "D 1", "D -1", "D -1", "I 5", "I 6"])) # [6,5]
