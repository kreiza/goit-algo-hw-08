import heapq

def merge_k_lists(lists):
    heap = []
    result = []

    # Додаємо перший елемент кожного списку до купи
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (значення, індекс списку, індекс елемента)

    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        result.append(val)

        # Додаємо наступний елемент з того ж списку, якщо він є
        if element_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][element_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, element_idx + 1))

    return result

# Приклад
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
