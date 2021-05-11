#p047.py
""" 서로 다른 두 개의 소인수를 갖는 수들이 처음으로 두 번 연달아 나오는 경우는 다음과 같습니다.
14 = 2 × 7
15 = 3 × 5

서로 다른 세 개의 소인수를 갖는 수들이 처음으로 세 번 연속되는 경우는 다음과 같습니다.
644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19

서로 다른 네 개의 소인수를 갖는 수들이 처음으로 네 번 연속되는 경우를 찾으세요. 그 첫번째 수는 얼마입니까? """

import time
start = time.time()

# [풀이 1] 소인수분해 함수 작성 후, 소인수 개수가 4개인 수가 연속되는 경우를 출력하도록 함. p_factor 함수를 사용하지 않은 경우, 100001부터 전수검사를 해도 264초 이상 소요됨.
# def factorization(n):
#
#     def p_factor(k):  # 소인수분해를 위해 나누는 수를 계산하는 함수 추가시 속도 개선됨 : 1부터 전수검사시 3초 미만 소요.
#         if k < 3: return k + 1
#         if k == 3: return 5
#         l = int(n ** 0.5 + 1.5)
#         j = k if k % 3 == 2 else k + 4
#         while j < l:
#             if n % j == 0: return j
#             if n % (j + 2) == 0: return j + 2
#             j += 6
#         return int(n)
#
#     f = []
#     i = 1
#     while n > 1: 
#         i = p_factor(i)
#         count = 0
#         while n % i == 0:
#             count += 1
#             n /= i
#         if count > 0:
#             f.append((i, count))
#     return f
#
# i, j = 2, 0  # 숫자(i)를 증가시키면서, 소인수가 네 개인 수가 연속으로 네 번(j : 0-1-2-3) 나올 때 종료
# while j < 4:  
#     j = j + 1 if len(factorization(i)) == 4 else 0
#     i += 1
# print(i-4)
# print(factorization(i-4), factorization(i-3), factorization(i-2), factorization(i-1))
#
# # i = 1  # 이 방법보다 위 방법이 0.5초 정도 단축
# # while True:
# #     i += 1
# #     if len(factorization(i)) < 4: continue  
# #     if len(factorization(i+1)) < 4: continue
# #     if len(factorization(i+2)) < 4: continue
# #     if len(factorization(i+3)) < 4: continue  
# #     print(i)
# #     print(factorization(i), factorization(i+1), factorization(i+2), factorization(i+3))
# #     break


# [풀이 2] 서로 다른 소인수 개수를 정리한 리스트를 만들어서, 값 4가 네 번 연속되는 구간을 찾는 방법(개수만 확인) : 0.86s(+)

# 서로 다른 소인수 개수 확인하기
MAX = 10**6 # 임의의 범위 설정
f = [0]*MAX
for i in range(2, MAX): 
    if f[i] == 0:   # i == 0, 즉, i가 소수이면(2부터 시작) i의 배수가 되는 항목들에 1씩 더해 준다. 소수 i의 배수는 i를 소인수로 갖고 있음. 
        for j in range(i, MAX, i):
            f[j] += 1     

# 같은 수의 소인수 개수가 연속되는 구간 확인하기
for i in range(2, MAX): # 4번 연속으로 4가 나오면 출력하고 종료. 
    if f[i] == 4:
        if f[i+1] == 4:
            if f[i+2] == 4:
                if f[i+3] == 4: 
                    print(i); break
                else: i += 3
            else: i += 2
        else: i += 1





print(time.time()-start)