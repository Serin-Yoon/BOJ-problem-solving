T = int(input())

#VPS 판별 함수
def isVPS(data):
    stack = []
    result = 1
    #입력 데이터 길이만큼 실행
    for i in range(len(data)):
        if data[i] == '(':
            stack.append(data[i])
        elif data[i] == ')':
            #제거할 '(' 존재하는 경우
            if len(stack) > 0:
                del stack[-1]
            #제거할 '(' 존재하지 않는 경우 VPS가 아님
            else:
                result = 0
                break
    #'('가 모두 제거되어 stack이 비어있는 경우 VPS임
    if (len(stack) == 0 and result == 1):
        print("YES")
    else:
        print("NO")

for i in range(T):
    isVPS(input())