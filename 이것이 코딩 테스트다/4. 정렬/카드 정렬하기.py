N = int(input())

cards = []

for i in range(N):
    cards.append(int(input()))

# 최소한의 비교를 위해 카드 수 오름차순 정렬
cards.sort()

total = 0

# 카드 한 장만 남을 때까지(모두 합쳐질 때까지) 첫번째 카드와 두번째 카드 합침
while len(cards) > 1:
    sum = cards[0] + cards[1]
    total += sum
    del cards[0]
    del cards[0]
    cards.insert(0, sum)

print(total)