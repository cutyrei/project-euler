# p033.py
""" 분수 49/98에는 재미있는 성질이 있습니다. 수학을 잘 모르는 사람이 분모와 분자에서 9를 각각 지워서 간단히 하려고 49/98 = 4/8 처럼 계산해도 올바른 결과가 됩니다.
이에 비해 30/50 = 3/5 같은 경우는 다소 진부한 예라고 볼 수 있습니다.
위와 같은 성질을 가지면서 '진부하지 않은' 분수는, 값이 1보다 작고 분자와 분모가 2자리 정수인 경우 모두 4개가 있습니다.
이 4개의 분수를 곱해서 약분했을 때 분모는 얼마입니까? """

# 1. 범위 : 분자/분모는 각각 두 자리 수, 분수의 값은 1 미만, 분자/분모가 모두 10의 배수인 경우는 제외, 분자와 분모에 0이 있는 경우 제외, 분자와 분모에 공통 수가 없는 경우 제외
# 2. 분자와 분모를 각각 리스트로 변환 후 같은 원소를 제외하고 만든 분수의 값과, 본래 분수 값이 같은지 비교 
# def f(a, b):
#     m = list(str(a))
#     n = list(str(b))
#     for i in m:
#         for j in n:
#             if i == j:
#                 m.remove(i)
#                 n.remove(j)
#     if '0' in m or '0' in n or len(m) > 1 or len(n) > 1 :
#         return False
#     return int(''.join(m)) / int(''.join(n))
# for a in range(98, 10, -1):
#     for b in range(99, 11, -1):
#         if a / b >= 1: break
#         if a % 10 == 0 and b % 10 == 0: break
#         if f(a, b) and a / b == f(a, b):
#             print(a, b, a/b, f(a, b))    

# # [풀이 2] ab/bc=e 일 때 b를 제외하면 a/c=e인 수를 찾아야 한다(단, e<1이고, ab와 bc는 2자리수)
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if a < c:   # a/c=e라면 e가 1보다 작아야 하므로, a가 c보다 작은 경우만 해당
                if (a*10 + b) / (b*10 + c) == a / c:
                    print(a, b, b, c)

# # [풀이 3] 각 두 자리 수(십단위-10으로 나눔)들을 몫과 나머지를 이용해 분해한 후, ab/bc == a/c를 구함
# col1 = []
# col2 = []
# for i in range(11, 100):
#     for j in range(10, i):
#         i1, i2 = divmod(i, 10)    # 11이라면, 1과 1로 분해
#         j1, j2 = divmod(j, 10)    # 10이라면, 1과 0으로 분해
#         if i2 * j2 == 0 or i % 11 == 0 or i == j: continue # 분자/분모가 10 또는 11의 배수이거나, 분자/분모가 같은 수인 경우 제외
#         if [j, i] not in col1:
#             if i1 == j2 and j / i == j1 / i2:
#                 col1.append([j, i])
#                 col2.append([j1, i2])
#             if i2 == j1 and j / i == j2 / i1:
#                 col1.append([j, i])
#                 col2.append([j2, i1])
# print(col1, col2)