import sys
from typing import List

input = sys.stdin.readline

N = int(input())

card: List[int] = [_ for _ in range(1, N + 1)]

point = 0
while point < len(card) - 1:
    point += 1
    data = card[point]
    card.append(data)
    point += 1

print(card[-1])