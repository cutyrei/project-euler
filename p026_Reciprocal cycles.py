#p026.py
""" 분자가 1인 분수를 단위분수라고 합니다. 분모가 2에서 10까지의 단위분수는 아래와 같습니다.
1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10 = 	0.1
1/6의 경우 순환마디는 "6"으로 0.166666...처럼 6이 무한히 반복됨을 뜻합니다. 같은 식으로 1/7은 6자리의 순환마디(142857)를 가집니다.

d 를 1000 이하의 정수라고 할 때, 단위분수 1/d 의 순환마디가 가장 긴 수는 무엇입니까? """

# [참고] 1. 하나의 긴 문자열(string)에서 반복하는 문자열(substrings)을 찾아 몇 번 반복하는지 확인
# 2. string의 길이를 정해야 하고, substring의 반복 확인은 string의 중간까지만 : 가장 긴 문자열이 반복된다면 반복수는 2번.
# 3. 만약 substring이 반복된다면, string은 substring의 길이(글자 개수)로 나누어 떨어져야 한다.
# def test(string):
#     x = len(string)
#     for i in range(1, (x//2)+1):
#         if x % i == 0:  # 이 조건이 유효하려면 string의 끝이 sub가 반복된 끝과 맞아 떨어져야 함. 
#             substrings = string[0:i]
#             repeat = x//i
#             if substrings*repeat == string:
#                 return '('+substrings+')'+'_'+str(repeat)
#     return string    
# print(test('142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857142857')) # 반복범위로 맞아 떨어져야만 가능

# [풀이1] 소수 부분을 문자열로 바꾼 뒤, 문자열을 다양한 크기로 자르고 그 다음 구간에 95% 이상을 대체할 수 있는 같은 패턴이 존재하는지 검사해서 순환마디를 판단하는 방법(opentutorials)
# from decimal import *

# def get_cycle_string(string):
#     length = len(string)
#     for i, v in enumerate(string):
#         end = int(string.find(v, i+1))
#         while end != -1 and end < length*0.5:
#             target = string[i:end]
#             target_len = end-i
#             test = string[end:end+target_len]
#             if target == test and string.count(target)*target_len > length*0.9:
#                 return target
#             else:
#                 end = int(string.find(v, end+1))

# decimalSize = 2000
# getcontext().prec = decimalSize
# max_length = 0
# for d in range(1, 1000):
#     string = str(Decimal(1)/Decimal(d))
#     string = string[string.find(".")+1:]
#     cycle = get_cycle_string(string)
#     if not cycle == None and len(cycle) > max_length:
#         max_length = len(cycle)
#         print(d, max_length)


# # [풀이2] 반복주기가 발생하는 나머지 리스트의 길이로 판단. 한 반복주기 안에서 몫은 중복될 수 있지만 나머지는 중복되지 않음.
# # 1/n의 순환마디 개수 구하는 함수(r=>1로 처음 나눌 때의 나머지 1)
# def repeat(n):
#     remainders = []
#     #quotiens = []
#     r = 1
#     while r != 0:
#         # r = r * 10
#         q, r = divmod(10*r, n)
#         if r in remainders:
#             #return [len(remainders), quotiens]
#             return len(remainders)
#         else:
#             remainders.append(r)
#             #quotiens.append(q)
#     return 0

# # max = 0; max_i = 0
# # for i in range(2, 1001):
# #     if max < int(repeat(i)):
# #         max = int(repeat(i))
# #         max_i = i
# # print(max_i, "일 때, 반복개수", max)
# print(max(range(2, 1001), key = lambda k: repeat(k)))

# [풀이3] 1. 분모가 2나 5 이외의 소인수를 가지면 순환소수. 
# 2. 순환소수 1/n의 분모가 n = n0 x 2^a x 2^b 일때 순환마디의 길이 k는 (10^k - 1)을 n0로 나누었을 때, 나누어 떨어지게 하는 가장 작은 수
max_cycle = 0
d = 0
for n in range(2, 1000):
    if n % 2 != 0 and n % 5 != 0:
        c = 1
        while (10 ** c) % n != 1:
            c += 1
        if c > max_cycle:
            max_cycle = c
            d = n
            #print(max_cycle, d)
print(max_cycle, d)




