# p049.py
""" 1487, 4817, 8147은 3330씩 늘어나는 등차수열(arithmetic sequence)입니다. 이 수열에는 특이한 점이 두 가지 있습니다.
(i) 세 수는 모두 소수입니다.
(ii) 세 수는 각각 다른 수의 자릿수를 바꿔서 만들 수 있는 순열(permutation)입니다.
1자리, 2자리, 3자리의 소수 중에서는 위와 같은 성질을 갖는 수열이 존재하지 않습니다. 하지만 4자리라면 위의 것 말고도 또 다른 수열이 존재합니다.
그 수열의 세 항을 이었을 때 만들어지는 12자리 수는 무엇입니까? """
import time
start = time.time()

# [풀이 1] 4자리 소수 중에서, 등차수열이면서 순열 조건을 만족하는 세 개의 소수를 구하기 : 0.4s(-)
# (1) 소수를 리스트에 담는 것보다 집합자료로 색인을 만드는 것이 실행시간을 단축 시킴(p_nums가 리스트일 경우 7s(-) vs. 집합인 경우 0.4s(-))
# (2) 문제를 근거로 조건을 더 축약시키면(소수 리스트 조건, 등차수열의 공차 조건) 0.02s(+)까지 단축 <= 등차수열의 공차가 3330인 것은 근거가 필요
#
p_nums = set() # 소수 집합
for i in range(1111, 10000):
# #for i in range(1489, 10000, 2):
    for j in range(2, int(i**0.5)+1):
        if i % j == 0: break
    else:
        p_nums.add(i)

for i in p_nums:
    for j in p_nums:
        if j <= i: continue
        if j + j - i not in p_nums: continue 
        if sorted(str(i)) == sorted(str(j)) == sorted(str(j + j - i)):
            print(i, j, j+j-i, "공차:", j-i, "12-digits:", str(i)+str(j)+str(j+j-i))
#     # if i+3330 in p_nums and i+6660 in p_nums and set(str(i)) == set(str(i+3330)) == set(str(i+6660)):
#     #     print(i, i+3330, i+6660, str(i)+str(i+3330)+str(i+6660))


# [풀이 2] 소수체로 4자리 소수를 구한 뒤, 각 소수를 정렬한 문자열이 key가 되는 dict() 생성(문자열:[정수]) -> 순열인 소수끼리 정리됨
# dict()의 값 중에서 원소가 3개 이상이고, 3개의 원소가 등차수열을 이루는 값을 찾는다 : 실행시간 0.007s(-)
# https://soooprmx.com/%EC%98%A4%EC%9D%BC%EB%9F%AC-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-49/
#
# limit = 10000
#
# # 10000 이하의 소수를 찾기위한 소수 체
# sieve = [False, False] + [True] * (limit - 1)
# for i in range(2, int(limit**0.5 + 0.5)):
#     if sieve[i]:
#         sieve[i*2::i] = [False] * ((limit - i) // i)
#
# # 네자리 소수 전체 목록
# primes = [x for x in range(1000,10000) if sieve[x]]
#
# # 순열을 구분하기 위한 문자열 key 생성
# def make_key(n):
#     return "".join(sorted(str(n)))
#
# # 등차수열 찾기
# def find_sequences(l):
#     l = sorted(l)
#     for i, a in enumerate(l[:-2]):
#         remain = l[i+1:]
#         for b in remain:
#             c = b * 2 - a
#             if c in remain:
#                 print("".join(str(x) for x in (a, b, c)))
#                 return
#               
# def main(): 
#     # dict() 만들기(key:[순열])
#     d = {}  
#     for p in primes:
#         key = make_key(p)
#         if key not in d:
#             d[key] = [p]
#         else:
#             d[key].append(p)
#     # 세 개 이상의 원소가 순열인 값 중에 세 원소가 등차수열인 경우 찾기
#     b = [x for x in d.values() if len(x) >= 3]
#     for x in b:
#         find_sequences(x)
#
# main()

print(time.time()-start)


