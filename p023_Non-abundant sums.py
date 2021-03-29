# p023.py
""" 자신을 제외한 약수(진약수, proper divisors)를 모두 더하면 자기 자신이 되는 수를 완전수(a perfect number)라고 합니다.
예를 들어 28은 1 + 2 + 4 + 7 + 14 = 28 이므로 완전수입니다.
또, 진약수의 합이 자신보다 작으면 부족수(deficient), 자신보다 클 때는 과잉수(abundants)라고 합니다.

12는 1 + 2 + 3 + 4 + 6 = 16 > 12 로서 과잉수 중에서는 가장 작습니다.
따라서 과잉수 두 개의 합으로 나타낼 수 있는 수 중 가장 작은 수는 24 (= 12 + 12) 입니다.

해석학적인 방법을 사용하면, 28123을 넘는 모든 정수는 두 과잉수의 합으로 표현 가능함을 보일 수가 있습니다.
두 과잉수의 합으로 나타낼 수 없는 가장 큰 수는 실제로는 이 한계값보다 작지만, 해석학적인 방법으로는 더 이상 이 한계값을 낮출 수 없다고 합니다.

그렇다면, 과잉수 두 개의 합으로 나타낼 수 없는 모든 양의 정수의 합은 얼마입니까? """

import time
start = time.time()


# 진약수의 합을 구하는 함수
def divSum(num):
    # sum = 0
    # for i in range(1, int(num/2)+1):
    #     if num % i == 0:
    #         sum += i
    # return sum # 아래 로직이 더 빠름
    sum = 1
    k = int(num**0.5)
    for i in range(2, k+1):
        if num % i == 0:
            quotient = 0 if (num//i==i) else (num//i) # 아래 if else 를 삼항연산자로 처리
            sum += i + quotient
            # if num // i == i:
            #     sum += i
            # else:
            #     sum += i + (num // i)
    return sum

# def is_perfect_num(num):
#     return num == divSum(num)
# num = 10000
# print(list(i for i in range(2, num+1) if is_perfect_num(i)))

numbers = list(range(1, 28124))    # 1~28123까지의 정수

"""
# 과잉수를 모두 찾고, 과잉수의 합을 찾아서 계산 : 12~13초 소요
abundants = list(filter(lambda x : x < divSum(x), numbers))   # 1~28123 사이의 과잉수
aSums = set()      # 두 개의 과잉수의 합으로 만들어지는 수(집합자료형으로 중복 수 제거)
for a in abundants:
    for b in abundants:
        if a + b < 28124:
            aSums.add(a + b)
"""
# 과잉수를 찾으면서, 과잉수의 합을 동시에 계산 : 8초 소요
abundants = []
aSums = set()
for i in range(1, 28124):
    if divSum(i) > i:
        abundants.append(i)
        for j in range(len(abundants)):
            if i + abundants[j] < 28124:
                aSums.add(i + abundants[j])

print(sum(numbers))
print(sum(aSums))
print(sum(numbers)-sum(aSums))


print(time.time()-start)