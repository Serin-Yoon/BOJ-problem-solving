import re
import sys

input = sys.stdin.readline #시간초과 에러 방지용

stack = []

N = int(input())

for i in range(N):
    command = input()
    if 'push' in command:
        #입력받은 문자열 중 숫자 추출 (문자 형태로 추출됨)
        data = re.findall("\d+", command)
        #정수 형태로 삽입
        stack.append(int(data[0]))
    elif 'pop' in command:
        if (len(stack) == 0):
            print("-1")
        else:
            print(stack[-1])
            del stack[-1]
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
        if len(stack) == 0:
            print("1")
        else: print("0")
    elif 'top' in command:
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])