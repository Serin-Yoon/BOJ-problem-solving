import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []
heapq.heapify(heap)

for i in range(N):
    data = int(input())
    if data == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-data, data))