# p046.py
""" 크리스티안 골드바흐는 모든 홀수인 합성수를 (소수 + 2×제곱수)로 나타낼 수 있다고 주장했습니다.
9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2
그러나 이 추측은 잘못되었음이 밝혀졌습니다.
위와 같은 방법으로 나타낼 수 없는 가장 작은 홀수 합성수는 얼마입니까? """
import time
start = time.time()


# [풀이 1] 홀수를 증가시키면서 소수 리스트를 만들고, 합성수인 경우 자기보다 작은 소수를 뺀 값이 2*(n^2)를 만족하는지 확인 : 0.08s(+)
# 홀수인 합성수(i) = 소수(j) + k(=2*(n^2)) => i, j, k는 자연수

def is_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

p = [2]
i = 1
not_found = True
while not_found:
    i += 2
    if is_prime(i): p.append(i)
    else:
        for j in p:
            k = i - j
            n = (k/2)**0.5
            if n == int(n): break
        else:
            not_found = False

print(i)

print(time.time()-start)


