# p056.py
""" 구골(googol)은 10^100을 일컫는 말로, 1 뒤에 0이 백 개나 붙는 어마어마한 수입니다.
100^100은 1 뒤에 0이 2백 개가 붙으니 상상을 초월할만큼 크다 하겠습니다.
하지만 이 수들이 얼마나 크건간에, 각 자릿수를 모두 합하면 둘 다 겨우 1밖에 되지 않습니다.
a, b < 100 인 자연수 a^b 에 대해서, 자릿수의 합이 최대인 경우 그 값은 얼마입니까? """

import time
start = time.time()

def digit_sum(n):
    a = str(n)
    sum = 0
    for i in a:
        sum += int(i)
    return sum

max = 0
for a in range(100):
    for b in range(100):
        if digit_sum(a**b) > max:
            max = digit_sum(a**b)

print(max)

print(time.time()-start)
