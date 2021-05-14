# p050.py
""" 41은 소수이면서 다음과 같은 6개의 연속된 소수의 합으로도 나타낼 수 있습니다.
41 = 2 + 3 + 5 + 7 + 11 + 13
이것은 100 이하에서는 가장 길게 연속된 소수의 합으로 이루어진 소수입니다.
1000 이하에서는 953이 연속된 소수 21개의 합으로 가장 깁니다.
1백만 이하에서는 어떤 소수가 가장 길게 연속되는 소수의 합으로 표현될 수 있습니까? """

import time
start = time.time()

# [풀이 1] 1백만 이하 소수의 누적 합 리스트에서, 누적 합 사이의 차가 가장 큰 두 지점(=연속 길이가 가장 긴 지점)을 찾는다 : 0.02s(-)
# a < b 일 때: b까지의 누적 합 S(b) - a까지의 누적 합 s(a) = a에서 b까지의 누적 합 s(b, a) => a에서 b까지는 연속 구간

def is_prime(n):    
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def p_sum(n):
    sums = [0]
    s = 0
    p = 2
    while s < n:
        if is_prime(p):
            s += p
            sums.append(s)
        p += 1
    return sums

limit = 1000000
primes_sum = p_sum(limit)   # 100만 이하 소수 누적 합 리스트(소수 확인과 합 누적을 병행)
max_d = 0   # 연속 구간의 길이
max_s = 0   # 연속 구간의 누적 합
for a in range(0, len(primes_sum)):
    for b in range(a+max_d, len(primes_sum)):    # a가 증가할 때 b의 시작은 이전까지의 합은 의미 없으므로 max_d 만큼 증가한 후 계산
        s = primes_sum[b] - primes_sum[a-1]        # a에서 b까지의 누적 합
        if is_prime(s) and (b-a) > max_d:
            max_d = b-a+1
            max_s = s
        if s > limit:
            break
print(max_s, max_d)


# [풀이 2] 소수 리스트에서 연속 구간이 가장 긴 구간부터 짧은 구간으로 검색하면서 조건을 만족하는지 찾아본다.
# 이 때, 연속된 소수의 합이 limit 이하여야 하므로 limit의 제곱근의 2배가 되는 수열까지로 검색 구간을 초기화한다. 
# => 자연수 1~n 까지의 합 : S(n) = n(n+1)/2 이므로, n -> S(n)^(1/2)*2 정도가 됨 : 검색구간 적용시 0.4s(+), 전체를 검색하면 53s(+)
#
# # (1) 소수 리스트
# def p_list(n):
#     seive = [1]*(n+1)
#     seive[:2] = [0, 0]
#     for i in range(2, int(n**0.5)+1):
#         if seive[i]:
#             for j in range(i*2, n+1, i):
#                 seive[j] = 0
#     return [i for i, n in enumerate(seive) if seive[i]]
#
# # (2) 가장 긴 연속 구간에서부터 구간을 줄여가면서 조건을 만족하는 합이 나올 때까지 찾는다.
# limit = 1000000
# primes = p_list(limit)
# print(primes)
# set_p = set(primes)
# for i in range(int(limit**0.5)*2, 0, -1): 
#     chk = False
#     for j in range(0, len(primes)):        
#         if sum(primes[j:i+j]) > limit: break  # [j:i+j] - 구간 초기화시 설정한 값 뒤의 숫자들까지 포함하여 검색
#         if sum(primes[j:i+j]) in primes:
#             print(sum(primes[j:i+j]), i)  # 맨 처음 조건을 만족하는 값을 출력하고 종료
#             chk = True
#             break
#     if chk == True: break


print(time.time()-start)