# p060.py
""" 네 개의 소수 3, 7, 109, 673은 상당히 특이한 성질이 있습니다. 넷 중에 아무것이나 두 개를 골라서 어떤 쪽으로 이어붙이던지 그 결과도 소수가 됩니다. 
예를 들어 7과 109를 고르면 7109와 1097 또한 소수입니다. 3, 7, 109, 673는 이런 성질을 가진 네 소수 중에서 그 합이 792로 가장 작습니다,
다섯 소수 중에 어떤 두 개를 골라 이어붙여도 소수가 되는 수들을 찾아서, 그 합의 최솟값을 구하세요. """

import time
start = time.time()

# [풀이 1] 임의로 설정한 범위(10000) 내 소수 들 중에서, 2개 > 3개 > 4개 > 5개로 조건에 맞는 수를 찾아 봄 : 100s(-)
# 소수 판별 함수를 그냥 사용할 때는 100s(-) 소요 => @ functools.lru_cache를 통한 메모이제이션 사용시 28s(-)까지 단축
#
import itertools, functools

@functools.lru_cache
def is_prime(n):    
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def prime_pair(list):
    pair_set = itertools.permutations(list, 2)
    for i in pair_set:
        temp = str(i[0])+str(i[1])
        if not is_prime(int(temp)):
            return False
    return True

primes = [x for x in range(3, 10**4, 2) if is_prime(x)]
chk = True
for p1 in range(len(primes)-4):
    for p2 in range(p1+1, len(primes)-3):
        if not prime_pair([primes[p1], primes[p2]]): continue
        for p3 in range(p2+1, len(primes)-2):
            if not prime_pair([primes[p1], primes[p2], primes[p3]]): continue
            for p4 in range(p3+1, len(primes)-1):
                if not prime_pair([primes[p1], primes[p2], primes[p3], primes[p4]]): continue
                for p5 in range(p4+1, len(primes)):
                    if not prime_pair([primes[p1], primes[p2], primes[p3], primes[p4], primes[p5]]): continue
                    print(primes[p1], primes[p2], primes[p3], primes[p4], primes[p5])
                    print(sum([primes[p1], primes[p2], primes[p3], primes[p4], primes[p5]]))
                    chk = False
    if chk == False: break


##############################################################################################################
# [풀이 2] 2s(-)
# 홀수 소수의 부분집합 P에서 작은 순서대로 a를 정하고 이 소수에 앞뒤로 붙어 소수가 되는 부분집합 R을 구합니다.
# 그런 다음 R에서 조건을 만족하는 4개짜리 소수 집합을 구할 수 있다면 여기에 a를 더해 답이 됩니다. 
# 이 과정을 재귀적으로 처리해봅니다. 4자리 소수범위에서 시작하고 답을 못찾으면 자리 수를 늘려가면서 계속 검사해봅니다. 
# ??? 문제의 예시와 같이 10**3 이내 소수 중에서 4개를 찾으려고 하면 다른 값이 나옴.

# def memoize(f):
#     m = dict()
#     def i(n):
#         if n in m: return m[n]
#         r = f(n)
#         m[n] = r
#         return r
#     return i

# @memoize ## 메모이제이션을 적용한 소수검사
# def is_prime(n):
#     if n < 2: return False
#     if n in (2, 3): return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     if n < 10: return False
#     k, l = 5, n ** 0.5
#     while k <= l:
#         if n % k == 0 or n % (k+2) == 0:
#             return False
#         k += 6
#     return True

# ## 두 수를 앞뒤로 붙여서 소수가 되는지 검사
# def test(a, b):
#     m = int(f"{a}{b}")
#     n = int(f"{b}{a}")
#     return is_prime(m) and is_prime(n)

# ## 주어진 소수의 부분집합으로부터 조건에 맞는 부분집합을 구하는 함수
# def process(xs, level=0):
#     if level == 0: return set()
#     for a in sorted(xs):
#         ys = {x for x in xs if x != a and test(x, a)}
#         if len(ys) < level - 1:
#             continue
#         result = process(ys, level-1)
#         if result is not None:
#             result.add(a)
#             return result
#     return None

# def main():
#     l = 4
#     while True:
#         limit = 10**l
#         primes = {x for x in range(3, limit, 2) if is_prime(x)}
#         result = process(primes, 5)
#         if result != None:
#             print(sorted(result), sum(result))
#             break
#         l += 1
    
# main()

print(time.time()-start)