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
        pass

    def seclection_sort(self, lst: list) -> list:
        pass

    def quick_sort(self, lst: list) -> list:
        pass

    def merge_sort(self, lst: list) -> list:
        pass

    def heap_sort(self, lst: list) -> list:
        pass


assert Sort().insertion_sort([4, 2, 3, 1]) == [1, 2, 3, 4]
assert Sort().insertion_sort([-1, 5, 3, 4, 0]) == [-1, 0, 3, 4, 5]
assert Sort().insertion_sort([-1]) == [-1]
assert Sort().insertion_sort([]) == []


