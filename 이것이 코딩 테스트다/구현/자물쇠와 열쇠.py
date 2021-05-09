# key 90도 회전
def rotate(key):
    newKey = [[0] * keySize for _ in range(keySize)]
    for x in range(keySize):
        for y in range(keySize):
            newKey[y][keySize - x - 1] = key[x][y]
    return newKey

# key 넣어보기
def attach(startX, startY, key, lock):
    for x in range(startX, startX + keySize):
        for y in range(startY, startY + keySize):
            lock[x][y] = lock[x][y] + key[x - startX][y - startY]

    #가운데 모두 1인지 체크
    for x in range(keySize - 1, keySize + lockSize - 1):
        for y in range(keySize - 1, keySize + lockSize - 1):
            if lock[x][y] == 0 or lock[x][y] == 2:
                return 0
    return 1

# 최종적으로 이동/회전시키며 판별
def check(key, rotateCnt):

    if rotateCnt > 3:
        return 0

    for x in range(0, len(lock) - keySize + 1):
        for y in range(0, len(lock) - keySize + 1):
            res = attach(x, y, key, lock)
            if res:
                return 1
            else:
                key = rotate(key)
                rotateCnt += 1
                check(key, rotateCnt)
    return 0

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
tmpLock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

keySize = len(key) # M X M
lockSize = len(tmpLock) # N X N

lock = []
for i in range((keySize - 1) * 2 + lockSize):
    lock.append([0] * ((keySize - 1) * 2 + lockSize))

for x in range(keySize - 1, keySize + lockSize - 1):
    for y in range(keySize - 1, keySize + lockSize - 1):
        lock[x][y] = tmpLock[x - keySize + 1][y - keySize + 1]

if check(key, 0):
    print('true')