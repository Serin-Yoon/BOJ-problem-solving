import sys, re

input = sys.stdin.readline

N = int(input())

list = sorted(map(int, input().split()))

x = int(input())

ptr1 = 0
ptr2 = N - 1
count = 0

while (ptr1 != ptr2):
    add = list[ptr1] + list[ptr2]
    if add == x:
        count += 1
        ptr1 += 1
    elif add < x:
        ptr1 += 1
    else:
        ptr2 -= 1

print(count)