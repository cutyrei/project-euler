# p052.py
""" 125874를 2배 하면 251748이 되는데, 이 둘은 같은 숫자로 이루어져 있고 순서만 다릅니다.
2배, 3배, 4배, 5배, 6배의 결과도 같은 숫자로 이루어지는 가장 작은 수는 무엇입니까? """

import time
start = time.time()

# [풀이 1] 1로 시작하는 서로 다른 6개의 숫자로 이루어진 수 중에서 조건을 만족하는 수를 찾음 : 0.01s(+)
from itertools import permutations
nums = [x for x in permutations('023456789', 5)]
for n in nums:
    a = '1' + ''.join(n)    # 6x가 같은 자리수가 되려면 첫 자리는 1(뒤의 5자리에는 1이 들어올 수 없음).
    for i in range(2, 7):   # 2x, 3x, 4x, 5x, 6x
        if sorted(str(int(a)*i)) != sorted(a):
            break
    else:
        print(a)
        break
    # if all(sorted(str(int(a)*i)) == sorted(a) for i in (2,3,4,5,6)): # 위 for ~ else 구문을 all 함수로 처리할 때 위 구문보다 느림 : 0.07s
    #     print(a)
    #     break


# [풀이 2] 1/7의 순환마디를 알았다면... 한 줄로 종료.
# 142857은 1/7 = 0.142857142857142857⋯ => 소수점 아래 순환마디를 이루는 6개 숫자로, 가장 잘 알려진 십진법 순환수이다.
# 2, 3, 4, 5, 6을 차례로 곱할 경우 그 자신의 순환순열이 되고 각각 2/7, 3/7, 4/7, 5/7, 6/7의 순환마디가 된다.
#
# print(int(10 ** 6 / 7))


# [풀이 3] 순열을 만들지 않고 계산하는 방법 : 0.01s(+)
# M자리수 A가 있고, 이의 순열인 B가 있다고 할 때, A의 임의의 자리숫자 i에 대해서 A의 i와 B의 i의 차이는 9의 배수입니다(10^x*i - 10^y*i).
# 따라서 두 배 했을 때 순열이라는 것은 그 수가 9의 배수이며, 6차례에 걸쳐서 이 변환이 가능하다는 것은 최소 6자리 이상의 수라는 의미입니다. 
# 즉, 99999 부터 9씩 증가하여 1000000/6까지 검사합니다. 만약 이 구간에서 찾을 수 없다면 7자리로 진행합니다. 
# def p052():
#   def test(n):
#     s = sorted(str(n))
#     for i in range(2, 7):
#       if s != sorted(str(n * i)):
#         return False
#     return True  
#   for x in range(99999, 999999, 9):
#     if test(x):
#       print(x)
#       return
#
# p052()


print(time.time()-start)
