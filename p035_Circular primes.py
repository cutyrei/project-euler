# p035.py
""" 소수 중에서 각 자리의 숫자들을 순환시켜도 여전히 소수인 것을 원형 소수(circular prime)라고 합니다. 예를 들어 197은 971, 719가 모두 소수이므로 여기에 해당합니다.
이런 소수는 100 미만에 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97 처럼 13개가 있습니다.
그러면 1,000,000 미만에는 모두 몇 개나 있을까요? """

import time
start = time.time()

# # [풀이1] 100만 미만의 소수를 먼저 찾고, 그 소수들이 원형소수인지 확인 : 실행시간 2s(+)
# # n까지의 소수 리스트 만들기
# import math
# def primes(n):
#     if n > 1: #0, 1은 소수가 아니므로 제외 
#         sieve = [True] * (n+1) # true: prime, false: not prime. default: true
#         for i in range(2, int(math.sqrt(n))+1):
#             if sieve[i] == True:
#                 for j in range(i+i, n+1, i):
#                     sieve[j] = False
#         return [i for i in range(2, n+1) if sieve[i] == True]
# # 소수 확인하기
# def isPrime(n):
#     if n < 2: return False
#     if n == 2: return True
#     if n > 2:
#         for i in range(2, int(math.sqrt(n))+1):
#             if n % i == 0:
#                 return False
#         return True
# # 숫자 순환(abc > bca > cab) 후 소수 판별하기
# def circular_p(n):
#     a = str(n)    
#     for i in range(len(a)):  
#         a = a[1:] + a[0]
#         if not isPrime(int(a)):
#             return False
#     return True

# MAX = 1000000 
# circular_primes = []
# for c in primes(MAX):
#     if circular_p(c):
#         circular_primes.append(c)
# print(len(circular_primes))

# [풀이2] itertools.product 모듈을 사용한 풀이 : 실행시간 0.2s(-)
# 순환시킨 숫자 역시 소수가 되려면 본래 수는 '2,4,5,6,8,0' 중 하나라도 포함해서는 안됨(짝수가 되거나 5의 배수가 되면 소수가 아님).
# 따라서, 1,3,7,9 만 사용해서 만들 수 있는 3자리 수부터 6자리 수까지의 조합이 원형소수가 됨
import math, itertools
def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return n != 1

count = 0
for i in range(3, 7): # 3자리 수에서 6자리 수(100 이상, 1000000 미만)
    for j in itertools.product('1379', repeat = i):  
        for k in range(len(j)):
            if not is_prime(int(''.join(j[k:]+j[:k]))):
                break
        else:
            count += 1
            print(j)

print(count + 13) # 100 이상 원형소수 + 100 미만 원형소수(13개)


print(time.time()-start)