import re
import sys

input = sys.stdin.readline

queue = []

N = int(input())
point = 0

for i in range(N):
    command = input()
    if 'push' in command:
        data = re.findall("\d+", command)
        queue.append(int(data[0]))

    elif 'pop' in command:
        if (len(queue) - point) <= 0:
            print("-1")
        else:
            print(queue[point])
            point += 1

    elif 'size' in command:
        print(len(queue) - point)

    elif 'empty' in command:
        if (len(queue) - point) <= 0:
            print("1")
        else:
            print("0")

    elif 'front' in command:
        if (len(queue) - point) <= 0:
            print("-1")
        else:
            print(queue[point])

    elif 'back' in command:
        if (len(queue) - point) <= 0:
            print("-1")
        else:
            print(queue[-1])

