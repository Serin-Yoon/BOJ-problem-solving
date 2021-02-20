import sys #시간초과 방지 목적

input = sys.stdin.readline

words = []

for _ in range(int(input())):
    data = input()[:-1] #\n 제거
    words.append((data, len(data))) #단어와 단어의 길이를 함께 저장

words = list(set(words)) #set 함수로 중복 요소 제거 후 리스트로 형변환

words.sort(key=lambda word: (word[1], word[0])) #단어 길이순 정렬 후 알파벳순 정렬

for word in words:
    print(word[0])