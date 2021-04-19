# p037.py
""" 소수 3797에는 왼쪽부터 자릿수를 하나씩 없애거나 (3797, 797, 97, 7) 오른쪽부터 없애도 (3797, 379, 37, 3) 모두 소수가 되는 성질이 있습니다.
이런 성질을 가진 소수는 단 11개만이 존재합니다. 이것을 모두 찾아서 합을 구하세요.
(참고: 2, 3, 5, 7은 제외합니다) """
import time
start = time.time()

# # [풀이1] 한 자리 수(2, 3, 5, 7) 제외, 10~19는 우절단시 소수 아니므로 제외, 짝수와 5의 배수 제외, 21부터 양면소수 조건을 만족하는 수가 11개가 될 때까지 반복 : 5.5s(+)
# def is_prime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return n != 1

# i = 19
# result = []
# while True:    
#     i += 2 # 홀수만 검사
#     if i % 5 == 0: continue
#     if is_prime(i):
#         a = str(i)
#         for k in range(1, len(a)):
#             if not is_prime(int(a[k:])) or not is_prime(int(a[:k])):
#                 break
#         else:
#             result.append(i)
#             print(result)
#     if len(result) == 11: break
# print(sum(result)) # 2,3,5,7을 포함하면 양면 소수는 모두 15개


# [풀이2] 숫자가 만들어지는 조건을 만족하는 경우만 확인하는 방법 : 0.3s(+)
#  - 첫째 자리는 2,3,5,7 만 올 수 있음(우절단시 맨 앞의 수만 남았을 때 소수여야 함)
#  - 마지막 자리는 3, 7 만 올 수 있음(짝수, 5의 배수, 0, 1, 9는 소수 아님)
#  - 그 외 가운데 숫자들은 1,3,7,9 만 올 수 있음

def is_prime(n):    # 소수 확인
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return n != 1

def check(n):
    s = str(n)
    if s[0] not in "2357": # 첫째 자리 수 확인
        return False
    for t in "024568": # 둘째 이후 자리 수 확인
        if t in s[1:]:
            return False
    return True

num = 13
result = []
while len(result) < 11:
    if num % 10 == 7:   # 끝자리가 7인 경우와 3인 경우만 확인
        num += 6
    elif num % 10 == 3:
        num += 4
    if check(num) and is_prime(num):
        for i in range(1, len(str(num))):
            if not is_prime(num % pow(10, i)) or not is_prime(num // pow(10, i)): # 좌우절단수를 10^n으로 나눌 때의 몫과 나머지로 확인할 수 있다.
                break
        else:
            result.append(num)
            print(result)
print(sum(result))


print(time.time()-start)