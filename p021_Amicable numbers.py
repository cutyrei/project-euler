# p021.py
""" n의 약수들 중에서 자신을 제외한 것의 합을 d(n)으로 정의했을 때,
서로 다른 두 정수 a, b에 대하여 d(a) = b 이고 d(b) = a 이면
a, b는 친화쌍(an amicable pair)이라 하고 a와 b를 각각 친화수(우애수, amicable numbers)라고 합니다.

예를 들어 220의 약수는 자신을 제외하면 1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110 이므로 그 합은 d(220) = 284 입니다.
또 284의 약수는 자신을 제외하면 1, 2, 4, 71, 142 이므로 d(284) = 220 입니다.
따라서 220과 284는 친화쌍이 됩니다.

10000 이하의 친화수들을 모두 찾아서 그 합을 구하세요. """

import time
start = time.time()

MAX = 10000
total = 0

# 자신을 제외한 약수의 합을 구하는 함수
def divisorSum(num):
    result = 0
    for i in range(1, num):
        if num % i == 0:
            result += i
    return result

# 친화수를 찾는다.
numbers = []
for i in range(1, MAX+1):
    if i in numbers: continue
    if divisorSum(divisorSum(i)) == i and divisorSum(i) != i:   # 'i의 약수의 합'과 'i의 약수의 합으로 구해진 값의 약수의 합'을 다시 구해서 비교 
        numbers.append(i)
        numbers.append(divisorSum(i))

# 친화수들의 합을 구한다.
print(numbers, sum(numbers))



print(time.time() - start)

