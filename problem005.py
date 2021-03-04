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

# from. codingdojang.com : 20 이하의 소수를 구한 후, 소수들의 곱을 구함 : 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 = 232792560

prime_num = [2]
for i in range(3, 20):
    for j in range(2, i):
        if i % j ==0:
            break
        elif j == i-1:
            prime_num.append(i)
#print(prime_num)

common_multiple = 1
for i in prime_num:
    while 1:
        if i * i > 20:
            common_multiple *= i
            break
        i *= i

print(common_multiple)
