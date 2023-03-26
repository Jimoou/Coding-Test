import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    food_queue = []
    for i, time in enumerate(food_times):
        heapq.heappush(food_queue, (time, i+1))
    
    total_time = 0
    previous_time = 0
    remaining_food = len(food_times)

    while total_time + (food_queue[0][0] - previous_time) * remaining_food <= k:
        current_time, food_idx = heapq.heappop(food_queue)
        total_time += (current_time - previous_time) * remaining_food
        remaining_food -= 1
        previous_time = current_time
    
    food_queue.sort(key=lambda x: x[1])
    return food_queue[(k - total_time) % remaining_food][1]