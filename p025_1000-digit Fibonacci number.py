#p025.py
""" 피보나치 수열은 아래와 같은 점화식으로 정의됩니다.

Fn = Fn-1 + Fn-2  (단, F1 = 1, F2 = 1).
이에 따라 수열을 12번째 항까지 차례대로 계산하면 다음과 같습니다.
F1 = 1, F2 = 1, F3 = 2, F4 = 3, F5 = 5, F6 = 8, F7 = 13, F8 = 21, F9 = 34, F10 = 55, F11 = 89, F12 = 144
수열의 값은 F12에서 처음으로 3자리가 됩니다.

피보나치 수열에서 값이 처음으로 1000자리가 되는 것은 몇번째 항입니까? """

import time
start = time.time()

# [풀이1] 자리수가 100개가 될 때까지 찾기
a, b, c = 1, 0, 0
i = 0
while len(str(c)) < 1000:    
    i += 1
    c = a + b
    a, b = b, c
print(i)
print(c)

""" # [풀이2] 피보나치수열을 짝수항/홀수항으로 구분하여 전개하는 방법
i, A, B = 3, 1, 1   # A, B가 1, 2항이고, i는 3항부터 시작
while True:
    if len(str(A+B)) == 1000:   # i항의 피보나치 수는 A+B, 피보나치 수의 길이가 1000일 때 종료
        print(i)
        #print(A+B)
        break
    else:
        if i % 2 == 0: A = A + B
        if i % 2 == 1: B = A + B
        i += 1 """


print("time: ", time.time()-start)

