import itertools

def BFS(lab, x, y):
    return

# 벽돌 3개 랜덤으로 세우기
def set(lab, three):

    print('원래 lab')
    for i in range(len(lab)):
        print(lab[i])

    newLab = lab[:]
    for one in three:
        newLab[one[0]][one[1]] = 1

    print('벽돌 놓은 후')
    for i in range(len(newLab)):
        print(newLab[i])

    return

        # 안전 영역 크기 확인 => 2인 곳마다 진행
        # virus = []
        # for x in range(N):
        #     for y in range(M):
        #         if lab[x][y] == 2:
        #             virus.append([x, y])


N, M = map(int, input().split()) #행N 열M

lab = []
for i in range(N):
    tmp = list(map(int, input().split()))
    lab.append(tmp)

visited = [[False] * M for _ in range(N)]

# 빈칸 좌표 리스트
empty = []
for x in range(N):
    for y in range(M):
        if lab[x][y] == 0:
            empty.append([x, y])
totalEmpty = len(empty)

# 벽돌 3개 랜덤 쌓기
selectList = list(itertools.combinations(empty, 3))

for three in selectList:
    set(lab, three)