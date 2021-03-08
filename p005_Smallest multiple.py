# problem005.py
""" 
1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까? 
"""
""" 
common_multiple = 2520
while common_multiple:
    common_multiple += 1
    for i in range(1, 21):
        if common_multiple % i !=0: break
    else:
        break
print(common_multiple) 
# 1~20의 최소공배수를 반복문으로 구하였으나, 연산시간이 오래 걸림.
"""

# from. codingdojang.com : MAX 이하의 소수들을 구하고, 각 소수들의 거듭제곱에 대해서 MAX 이하 최댓값 여부를 판단한 뒤, 그 값들을 모두 곱함.
# 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232792560

MAX = 20
prime_num = [2]

for i in range(3, MAX):
    for j in range(2, i):
        if i % j ==0:
            break
        elif j == i-1:
            prime_num.append(i)
#print(prime_num)

common_multiple = 1
for i in prime_num:
    while 1:
        if i * i > MAX:
            common_multiple *= i
            break
        i *= i

print(common_multiple)
