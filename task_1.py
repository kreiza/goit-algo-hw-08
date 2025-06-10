import heapq

def min_total_cost(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost

# Приклад
cable_lengths = [5, 2, 4, 3, 6]
print("Мінімальні загальні витрати:", min_total_cost(cable_lengths))
