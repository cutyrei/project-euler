#p014.py
""" 양의 정수 n에 대하여, 다음과 같은 계산 과정을 반복하기로 합니다.
n → n / 2 (n이 짝수일 때)
n → 3 n + 1 (n이 홀수일 때)

13에 대하여 위의 규칙을 적용해보면 아래처럼 10번의 과정을 통해 1이 됩니다.
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
아직 증명은 되지 않았지만, 이런 과정을 거치면 어떤 수로 시작해도 마지막에는 1로 끝나리라 생각됩니다.
(역주: 이것은 콜라츠 추측 Collatz Conjecture이라고 하며, 이런 수들을 우박수 hailstone sequence라 부르기도 합니다)

그러면, 백만(1,000,000) 이하의 수로 시작했을 때 1까지 도달하는데 가장 긴 과정을 거치는 수는 얼마입니까?
참고: 계산 과정에는 백만을 넘어가는 수가 나와도 괜찮습니다. """

import time
start = time.time()

""" # 짝수 홀수를 구분하고 1이 될 때까지 각각의 조건을 적용 계산하는 함수
def collatz(num):
    count = 0
    while num > 1:
        count += 1
        #print(int(num), end=' ')
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3*num + 1
    #print("last-num", num, "count", count)
    return count

# 1,000,000 이하의 수 중에서 과정이 가장 긴 수를 찾는다.
seq = 0         # 단계 수
number = 0      # 해당 숫자
for n in range(1000001):
    count = collatz(n)
    if count >= seq:
        seq, number = count, n
        #print("s", seq, "n", number)
print("s", seq, "n", number) # 연산시간 : 44초 이상"""

# 이전 숫자의 계산 결과를 딕셔너리에 저장해 두고, 이후 다른 숫자를 계산하는 과정에서 이전 숫자와 같은 수가 나오면 그 값을 재활용하여 연산 시간을 단축
dictionary = dict()
for n in range(1, 1000001):
    num = n
    count = 0
    while True:
        if n == 1:
            count += 1
            break
        if n in dictionary:
            count = count + dictionary[n]
            break
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1            
        count += 1
    dictionary[num] = count

max_step_num = max(dictionary, key=dictionary.get)
max_step = dictionary[max_step_num] 
print("가장 긴 과정을 거치는 수:", max_step_num, "단계 수:", max_step)

print("runnig time: ", time.time() - start)