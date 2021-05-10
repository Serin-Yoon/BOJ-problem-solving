N = int(input())

hall = []
teacher = []
student = []

for i in range(N):
    tmp = list(input().split())
    hall.append(tmp)
    for j in range(N):
        if hall[i][j] == 'T':
            teacher.append([i, j])
        elif hall[i][j] == 'S':
            student.append([i, j])
