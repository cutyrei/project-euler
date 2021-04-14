# p032.py
""" 영국의 화폐 단위는 파운드(£)와 펜스(p)이고, 동전의 종류는 아래와 같습니다.
1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), £2 (200p)
이 동전들을 가지고 2파운드를 만드는 방법은 다양할 것입니다. 예를 하나 들면 이렇습니다.
1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

2파운드를 만드는 서로 다른 방법은 모두 몇 가지나 있습니까? """

# 전체 동전을 조합하는 반복문의 경우 파이썬에서 시간이 너무 오래 걸림.
# Dynamic Programming
# ways[n] = value : n(index)은 금액, value는 n 금액을 만들 수 있는 횟수. ways[0]=1은, 전체 금액 '0원'을 만들 수 있는 회수는 아무 동전도 선택하지 않는 '1회'임을 의미.
# target = 200    # 만들고자 하는 금액
# coins = [1, 2, 5, 10, 20, 50, 100, 200]
# ways = [1] + [0]*target    
# for coin in coins:
#     for i in range(coin, target+1):
#         ways[i] += ways[i-coin]
# # for coin, i in [(coin, i) for coin in coins for i in range(coin, target+1)]: ways[i] += ways[i-coin]
# print(ways[-1])

# 위의 dp를 동전 개수와 만들 금액, 각 동전의 가치를 입력 받아 계산 하도록 함.
n = int(input("사용할 동전의 갯수를 입력 >>> "))
k = int(input("얼마를 만들까요? >>> "))
coins = []
for i in range(n):
    a = int(input(f"{i+1}번째 동전은 얼마짜리? >>> "))
    coins.append(a)
w = [1] + [0 for _ in range(k)]
for c in coins:
    for j in range(c, k+1):
        w[j] = w[j] + w[j-c]
#print(coins)
#print(w)
print(f"{k}(을)를 만들기 위한 동전 조합 경우의 수는 {w[-1]}.")

