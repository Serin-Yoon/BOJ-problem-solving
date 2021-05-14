N = int(input())

stuList = []

for i in range(N):
    name, kor, eng, math = input().split()
    stuList.append([name, int(kor), int(eng), int(math)])

# 국어 내림차순, 영어 오름차순, 수학 내림차순, 이름 오름차순 재정렬
stuList = sorted(stuList, key = lambda x : (-x[1], x[2], -x[3], x[0]))

for student in stuList:
    print(student[0])