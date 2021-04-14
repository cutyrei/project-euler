#p032.py
""" 1부터 n까지의 각 숫자를 한 번씩만 써서 만들 수 있는 수를 팬디지털(pandigital)이라고 합니다.
예를 들면 15234는 1부터 5의 숫자가 한 번씩만 쓰였으므로 1 ~ 5 팬디지털입니다.
7254라는 수는 그런 면에서 특이한데, 39 × 186 = 7254 라는 곱셈식을 만들 때 이것이 1 ~ 9 팬디지털이 되기 때문입니다.

이런 식으로 a × b = c 가 1 ~ 9 팬디지털이 되는 모든 c의 합은 얼마입니까?
(참고: 어떤 c는 두 개 이상의 (a, b)쌍에 대응될 수도 있는데, 이런 경우는 하나로 칩니다) """

# 1. 범위 : a*b=c에서 1~9의 숫자가 한 번씩 존재하려면, 각 자릿수의 합은 9여야 한다 >> 1자리(a)*4자리(b)=4자리(c) 또는 2자리(a)*3자리(b)=4자리(c) 만 가능(각 자리에는 중복 숫자 없음)
# 2. a, b, c(=a*b)를 모두 문자열로 붙인 후 오름차순으로 정렬했을 때 '123456789'라면, 1~9의 팬디지털이 된다.

import time
start = time.time()

pandigital = set()
for a in range(2, 99): # a는 1자리 또는 2자리
    for b in range(123, 9877): # b는 3자리 또는 4자리
        if (a*b) > 9999: break # a*b는 4자리
        if ''.join(sorted((str(a) + str(b) + str(a*b)))) == '123456789':
            pandigital.add(a*b)
            print(f"{a} * {b} = {a*b}")
print(pandigital)
print(sum(pandigital))

## 위의 반복문을 한 줄로 표현
#print(sum(set(a*b for a in range(2, 99) for b in range(123, 9877) if ''.join(sorted(str(a)+str(b)+str(a*b)))=='123456789' )))

# permutations 모듈을 사용하는 방법
# from itertools import permutations
# def f(p):
#     return int(''.join(list(p))) # permutations로 생성된 튜플자료를 숫자로 변환
# print(sum(set(list(f(p[5:]) for p in permutations('123456789') if f(p[0])*f(p[1:5])==f(p[5:]) or f(p[:2])*f(p[2:5])==f(p[5:])))))

print(time.time()-start)
