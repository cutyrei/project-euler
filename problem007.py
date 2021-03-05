# problem007.py

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" 
소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

이 때 10,001번째의 소수를 구하세요.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import time
start = time.time()

""" # [풀이 1] 반복문으로 길이가 10,001인 소수의 리스트를 만든다. 연산 시간 과다 => runnig time:  71.21816229820251

primes = [2]
num = 2

while len(primes) <= 10000:
    num += 1
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primes.append(num)
        # if len(primes) % 1000 == 0:
        #     print(len(primes), num)

print(primes[-1]) """


# [풀이2] 자연수의 크기를 임의로 정한 후(MAX), '에라토스테네스의 체'를 활용 => runnig time:  0.706892728805542

MAX = 1000000 # MAX 이하의 자연수 중에서 소수를 구함

bools = [False, False] + [True]*(MAX-1) #소수를 찾아내기 위한 비교 리스트 : True인 인덱스에 해당하는 값을 primes에 저장
primes = [] #소수만 보관하는 리스트

#에라토스테네스의 체(MAX가 주어지는 경우)
for i in range(2, MAX+1):
    if bools[i]:
        primes.append(i)
        for j in range (2*i, MAX+1, i):
            bools[j] = False

print(primes[10000])

print("runnig time: ", time.time() - start)