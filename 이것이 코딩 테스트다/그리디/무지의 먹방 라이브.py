def solution(food_times, K):
    i = 0
    time = 0
    while len(food_times) > 0:
        if food_times[i] == 0:
            del food_times[i]
        else:
            time += 1
            food_times[i] -= 1
        i += 1
        if i >= len(food_times):
            i -= len(food_times)
    return(time - K)

food_times = list(map(int, input().split()))
K = int(input())

print(solution(food_times, K))