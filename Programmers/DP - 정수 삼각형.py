from itertools import chain

def solution(triangle, idx):
    floor = len(triangle) # 몇 층까지 있는지
    cnt = floor * (floor + 1) // 2 # 전체 개수
    tmpTriangle = list(chain.from_iterable(triangle)) # 1차원 배열화
    case1 = False

    if idx == 0:
        dp[idx] = tmpTriangle[0]
    else:
        for i in range(1, floor):
            if idx * 2 == i * (i + 1) or (idx + 1) * 2 == i * (i + 1):
                case1 = True
                data = i

        #양끝쪽인 경우
        if case1:
            dp[idx] = solution(triangle, idx - data) + tmpTriangle[idx]
        #아닌 경우
        else:
            for i in range(1, floor):
                if i * (i + 1) // 2 < idx < (i + 1) * (i + 2) // 2:
                    dp[idx] = max(solution(triangle, idx - i), solution(triangle, idx - i - 1)) + tmpTriangle[idx]

    if 0 not in dp:
        print(max(dp))
        return
    else:
        return dp[idx]

    #return max(dp)


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4]]

floor = len(triangle) # 몇 층까지 있는지
cnt = floor * (floor + 1) // 2 # 전체 개수
dp = [0] * cnt

#print(dp)
for i in range(cnt):
    solution(triangle, i)
#print(max(dp))