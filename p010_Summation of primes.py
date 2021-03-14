#p010.py

""" 10 이하의 소수를 모두 더하면 2 + 3 + 5 + 7 = 17 이 됩니다.
이백만(2,000,000) 이하 소수의 합은 얼마입니까? """

import time
start = time.time()

MAX = 2000000
bools = [False, False] + [True]*(MAX-1)
primes = []
total = 0

for i in range(2, MAX+1):
    if bools[i]:
        total += i
        primes.append(i)
        for j in range(2*i, MAX+1, i):
            bools[j] = False

print(total)
print(len(primes))
print(primes)

print("runnig time: ", time.time() - start)