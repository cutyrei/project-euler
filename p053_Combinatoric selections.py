# p053.py
""" 1,2,3,4,5 다섯 숫자 중에서 세 개를 고르는 것에는 다음과 같은 10가지 경우가 있습니다.
123, 124, 125, 134, 135, 145, 234, 235, 245, 345
조합론에서는 이것을 5C3 = 10 또는 (5 3)=10 이라고 표기하며, 일반적인 식은 아래와 같습니다.
nCr = (n r) = n!/r!(n−r)!,  단 r ≤ n 이고, n! = n×(n−1)×...×3×2×1 이며, 0! = 1.
이 값은 n = 23 에 이르러서야 23C10 =(23 10)= 1144066 으로 처음 1백만을 넘게 됩니다.
1 ≤ n ≤ 100 일 때 nCr 값이 1백만을 넘는 경우는 모두 몇 번입니까? (단, 중복된 값은 각각 계산합니다) """

import time
start = time.time()

# [풀이 1] 그냥 문제대로 계산 : 0.01s
# import math
# count = 0
# for n in range(1, 101):
#     for r in range(1, n+1):
#         a = math.factorial(n) / (math.factorial(r)*math.factorial(n-r))
#         if a > 10**6:
#             count += 1
#             #print(n, r, a)
# print(count)


# [풀이 2] 파스칼의 삼각형을 이용 : 0.003s
p_nums = [1]*101
count = 0
for n in range(1, 101):
    p_nums[n] = 1
    for r in range(n-1, 0, -1):
        p_nums[r] = p_nums[r] + p_nums[r-1]
        if p_nums[r] > 10**6:
            count += 1
            p_nums[r] = 1000001
print(count)

print(time.time()-start)

