def solution(p):
    res = []
    open = []
    close = []
    for i in range(len(p)):
        res.append(p[i])
        if p[i] == '(':
            if close:
                changeIdx = close[-1]
                res[changeIdx] = '('
                res[i] = ')'
                del close[-1]
            else:
                open.append(i)  # 나중에 변환을 위해 인덱스 저장
        elif p[i] == ')':
            if open:
                del open[-1]
            else:
                close.append(i)

    print(''.join(res))
    return

p = input()

solution(p)