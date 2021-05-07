# p043.py

import time
from itertools import permutations
start = time.time()

#[풀이1] permutations 모듈로 0-9의 팬디지털 수를 만든 후, 문자열 슬라이싱으로 해당 조건 확인해서 찾는 방법 : 5.5s(+)
#
# results = []
# r = [2, 3, 5, 7, 11, 13, 17]
# numbers = permutations('0123456789')
# for num in numbers:
#     n = str(''.join(num))
#     if n[0] == '0': continue
#     for i in range(len(r)):
#         if int(n[(i+1):(i+4)]) % r[i] != 0:
#             break
#     else:
#         results.append(int(n))
#
# print(sum(results))

# [풀이2] 조건에 해당하는 수를 만들어서 합산하는 방법 : 0.002s(+)
# (1) 0-9로 마지막 세 자리가 17의 배수인 수의 리스트를 만든다().
# (2) 1의 결과에 왼 쪽으로 수를 하나씩 붙이면서, 제수 리스트(13,11,7,5,3,2)의 배수인지 확인하여 9자리 수의 리스트를 만든다(재귀 사용).
# (3) 마지막 한 자리 수를 붙여 10자리 팬디지털 수의 리스트를 완성한다.

# (1) 17의 배수인 끝 세 자리 수 만들기(제수 17, 0-9 숫자)
def mk_num(div):
    results = []
    for i in range(10):
        for j in range(10):
            if j == i: continue
            for k in range(10):
                if k == j or k == i: continue
                if int(str(i)+str(j)+str(k)) % div == 0:
                    results.append(str(i)+str(j)+str(k))
    return results

# (2) 재귀함수로 9자리 수까지 이어 붙이기(제수 리스트(divisors), 재귀 횟수, mk_num 결과 리스트)
def attach_num(div, n, r):
    src = r
    results = []
    for s in src:
        t = s[:2]
        for i in range(10):
            if str(i) in s: continue
            if int(str(i)+t) % div[n] == 0:
                results.append(str(i)+s)
    if div[n+1] != 0:
        n += 1
        return attach_num(div, n, results)            
    return results

# (3) 마지막 수를 붙여서 10자리 수를 완성하고 총합을 구하기(attach_num 결과 리스트)
def fin_num(r):
    src = r
    results = []
    for s in src:
        for i in range(1, 10):
            if str(i) in s: continue
            results.append(int(str(i)+s))
    return sum(results)

divisors = [13, 11, 7, 5, 3, 2, 0]  # 17은 mk_num에서 마지막 세자리 수 만들 때 사용, attach_num에서 오른 쪽부터 왼 쪽으로 확인해 갈 것이므로 13부터 시작하고 0은 재귀함수 종료에 사용
# a = mk_num(17)
# b = attach_num(divisors, 0, a)
# c = fin_num(b)
# print(a)
# print(b)
# print(c)
print(fin_num(attach_num(divisors, 0, mk_num(17))))



print(time.time()-start)
