# p027.py
""" 오일러는 다음과 같은 멋진 이차식을 제시했습니다.
n^2 + n + 41
이 식의 n에다 0부터 39 사이의 수를 넣으면, 그 결과는 모두 소수가 됩니다.
하지만 n = 40일 때의 값 40^2 + 40 + 41 은 40×(40 + 1) + 41 이므로 41로 나누어지고, n = 41일 때 역시 41^2 + 41 + 41 이므로(41로 나누어짐) 소수가 아닙니다.
컴퓨터의 발전에 힘입어 n^2 − 79n + 1601 이라는 엄청난 이차식이 발견되었는데, 이것은 n이 0에서 79 사이일 때 모두 80개의 소수를 만들어냅니다. 이 식의 계수의 곱은 -79 × 1601 = -126479가 됩니다.

아래와 같은 모양의 이차식이 있다고 가정했을 때,
n^2 + an + b   (단 | a | < 1000, | b | <= 1000)
0부터 시작하는 연속된 n에 대해 가장 많은 소수를 만들어내는 이차식을 찾아서, 그 계수 a와 b의 곱을 구하세요. """

import time
start = time.time()

# [풀이1] a, b, n의 반복문으로 수식(r)의 결과가 소수 연속 출력을 끝낼 때의 값을 구함 : 7초
# 소수 구하는 함수 : 소수면 True, 합성수면 False
# def isPrime(n): 
#     if (n % 2 == 0 and n > 2) or n <= 1: return False
#     for i in range(3, int(n**0.5)+1, 2):
#         if n % i == 0: return False
#     return True

# [참고] 문제 속 이차식 검증
# n = 0
# while n >= 0:
#     #r = pow(n, 2) + n + 41
#     #r = pow(n, 2) - 79*n + 1601
#     r = pow(n, 2) -61*n + 971
#     if r > 0 and isPrime(r): print(n, r, "True")
#     else: 
#         print(n, "False")
#         break
#     n += 1

# max = 0  # 소수를 연속으로 출력하는 최대 횟수
# for a in range(-999, 1000):
#     for b in range(-1000, 1001):
#         n = 0
#         while n >= 0:
#             r = pow(n, 2) + a*n + b
#             if r > 0 and isPrime(r): 
#                 n += 1
#             else:
#                 if n > max:
#                     max = n
#                     print("a:", a, "b:", b, "소수개수:", n-1, "r:", r, "a*b:", a*b)
#                     break
#                 else:
#                     break

# [풀이2] -999~999중에서 소수만 a와 b에 대입하여 계산 : 1초 미만
# n = 0 일 때, (n*n + a*n + b)가 소수여야 하므로 b는 소수. n = 1일 때, (1 + a + b)는 홀수인 소수(소수 중 짝수는 2만 존재)
import math
def prime_num_test(n):
    n = abs(n)
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def formula(a, b):
    x = 0
    while True:
        n = x*x + a*x + b
        if n < 0:
            return 0
        if prime_num_test(n):
            x += 1
        else:
            return x

prime_num_set = set(filter(prime_num_test, range(-999, 1000)))
start_time = time.time()
primes_num = 0
a0 = 0
b0 = 0
for a in prime_num_set:
    for b in prime_num_set:
        if primes_num < formula(a, b):
            primes_num = formula(a, b)
            a0 = a
            b0 = b

print("x^2 + ({0})x + {1} = 0 : primes_num = {2}, answer = {3}".format(a0, b0, primes_num, a0*b0))

# 프로그램 종료
print("time: ", time.time()-start)

        