# p041.py
""" 1부터 n까지의 숫자를 하나씩만 써서 만든 n자리 숫자를 팬디지털(pandigital)이라고 부릅니다.
2143은 4자리 팬디지털인데, 이 수는 동시에 소수이기도 합니다.
n자리 팬디지털 소수 중에서 가장 큰 수는 무엇입니까? """
import time
from itertools import permutations
start = time.time()

def is_prime(n):    # 소수 확인
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return n != 1

a = '987654321'
i = 7       # 배수판정법에서 1부터 9까지의 합 45는 3의배수이고, 1부터 8까지의 합 36은 3의배수라서 소수가 될 수 없음. 1부터 7까지의 순열만 고려함.
while i > 0:
    m = a[(len(a)-i):]
    n = permutations(m)
    for t in n:
        t = int(''.join(t))
        if t % 2 == 0: continue
        if is_prime(t): print(t); i = 0; break  # 제일 큰 수 찾은 후 반복식 종료시킴  
    i -= 1

print(time.time()-start)