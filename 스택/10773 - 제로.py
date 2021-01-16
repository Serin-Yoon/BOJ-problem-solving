K = int(input())

stack = []

for i in range(K):
    data = int(input())
    #0이 아닌 숫자를 말한 경우 삽입
    if data != 0:
        stack.append(data)
    #0을 말한 경우 마지막 숫자 삭제
    else:
        del stack[-1]

total = 0

for i in range(len(stack)):
    total += stack[i]

print(total)