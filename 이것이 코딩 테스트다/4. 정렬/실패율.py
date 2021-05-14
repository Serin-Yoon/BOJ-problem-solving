def solution(N, stages):
    people = len(stages) # 전체 플레이어 수
    fail = [0] * (N + 1) # stage별 실패자 수
    failRate = [] # [stage, 실패율] 2차원 배열

    # stage별 실패자 수 세기
    for stage in stages:
        fail[stage - 1] += 1

    # stage 별 실패율 구하기
    for i in range(N):
        if fail[i] == 0:
            failRate.append([i + 1, 0])
        else:
            num = fail[i] / people
            failRate.append([i + 1, num])
            people -= fail[i]

    # 실패율 높은 순, stage 번호 낮은 순 재정렬
    failRate = sorted(failRate, key = lambda x : (-x[1], x[0]))

    # 실패율 제거, stage 번호만 남김
    for i in range(len(failRate)):
        failRate[i] = failRate[i][0]

    return failRate

solution(4, [4, 4, 4, 4, 4])