# p039.py
""" 세 변의 길이가 모두 자연수 {a, b, c}인 직각삼각형의 둘레를 p 로 둘 때, p = 120 을 만족하는 직각삼각형은 아래와 같이 세 개가 있습니다.
{20, 48, 52}, {24, 45, 51}, {30, 40, 50}
1000 이하의 둘레 p에 대해서, 직각삼각형이 가장 많이 만들어지는 p의 값은 얼마입니까? """

import time
import math

start = time.time()

# [풀이1] 0.07s(+)
# 1. 직각삼각형 피타고라스 정리 : a^2 + b^2 = c^2 => c는 (a^2 + b^2)의 제곱근(c는 a와 b에 따라서 실수 또는 정수의 값이 됨)
# 2. 둘레 p = a+b+c는 1,000을 초과하지 않아야 하고, c는 자연수이어야 함.

MAX = 1000
p_table = [0 for _ in range(MAX+1)]
for a in range(1, MAX):
    for b in range(a+1, MAX):
        c = math.sqrt(a*a + b*b)
        p = a + b + int(c)
        if p > MAX: break
        if c == int(c):
            p_table[p] += 1
           # print(p, a, b, c)
print(max(p_table), p_table.index(max(p_table)))


print(time.time()-start)
