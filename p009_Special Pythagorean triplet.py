# p009.py

""" 세 자연수 a, b, c 가 피타고라스 정리 a^2 + b^2 = c^2 를 만족하면 피타고라스 수라고 부릅니다 (여기서 a < b < c ).
예를 들면 3^2 + 4^2 = 9 + 16 = 25 = 5^2이므로 3, 4, 5는 피타고라스 수입니다.

a + b + c = 1000 인 피타고라스 수 a, b, c는 한 가지 뿐입니다. 이 때, a × b × c 는 얼마입니까? """

import time
start = time.time()

# for a in range(1, 1001): #runnig time:  0.45581746101379395
#     for b in range(a+1, 1001):
#         c = 1000-a-b
#         if a**2 + b**2 == c**2:
#             print(a, b, c, a*b*c)
#             break


# runnig time:  0.3830451965332031
result = [(a, b, (1000-a-b)) for a in range(1, 1001) for b in range(a+1, 1001) if a**2 + b**2 == (1000-a-b)**2][0]
print(result)
print(result[0]*result[1]*result[2])


print("runnig time: ", time.time() - start)