class Sort:
    def insertion_sort(self, lst: list) -> list:
        for idx in range(len(lst) - 1):
            for cmp in range(idx, -1, -1):
                if lst[cmp] > lst[cmp+1]:
                    lst[cmp], lst[cmp+1] = lst[cmp+1], lst[cmp]
                else:
                    break

        return lst

    def bubble_sort(self, lst: list) -> list:
        for i in range(len(lst) - 1):
            for idx in range(len(lst) - 1 - i):
                if lst[idx] > lst[idx + 1]:
                    lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]

        return lst

    def seclection_sort(self, lst: list) -> list:
        for idx in range(len(lst)):
            mn = idx
            for j in range(idx + 1, len(lst)):
                if lst[j] < lst[mn]:
                    mn = j
            if idx != mn:
                lst[idx], lst[mn] = lst[mn], lst[idx]

        return lst

    def quick_sort(self, lst: list, start: int, end: int) -> list:
        if start >= end:
            return None

        pivot = lst[end]
        low = start
        high = end - 1

        while low <= high:
            while low <= end and lst[low] < pivot:
                low += 1
            while high >= start and lst[high] > pivot:
                high -= 1

            if low < high:
                lst[low], lst[high] = lst[high], lst[low]

        lst[low], lst[end] = lst[end], lst[low]

        self.quick_sort(lst, start, low-1)
        self.quick_sort(lst, low+1, end)

        return lst

    def merge(self, l_lst: list, r_lst: list) -> list:
        i = j = 0
        result = []

        while i < len(l_lst) and j < len(r_lst):
            if l_lst[i] < r_lst[j]:
                result.append(l_lst[i])
                i += 1
            else:
                result.append(r_lst[j])
                j += 1

        if i < len(l_lst):
            result.extend(l_lst[i:])

        if j < len(r_lst):
            result.extend(r_lst[j:])

        return result

    def merge_sort(self, lst: list) -> list:
        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2
        l_lst = lst[:mid]
        r_lst = lst[mid:]

        return self.merge(self.merge_sort(l_lst), self.merge_sort(r_lst))

    def heap_sort(self, lst: list) -> list:
        return lst


# assert Sort().insertion_sort([-1, 5, 3, 4, 0, 8, -3]) == [-3, -1, 0, 3, 4, 5, 8]
# assert Sort().seclection_sort([-1, 5, 3, 4, 0, 8, -3]) == [-3, -1, 0, 3, 4, 5, 8]
# assert Sort().bubble_sort([-1, 5, 3, 4, 0, 8, -3]) == [-3, -1, 0, 3, 4, 5, 8]
# assert Sort().quick_sort([-1, 5, 3, 4, 0, 8, -3], 0, 6) == [-3, -1, 0, 3, 4, 5, 8]
# print(Sort().quick_sort([45, 39, 98, 15, 52, 44, 33, 28, 40, 38, 77, 68, 11, 43], 0, 13))
print(Sort().merge_sort([45, 39, 98, 15, 52, 44, 33, 28, 40, 38, 77, 68, 11, 43]))
print(Sort().merge_sort([45, 3]))
