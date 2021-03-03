# problem003.py
# 600851475143의 소인수 중에서 가장 큰 수를 구하세요.

# 1. 소인수 분해를 한다.
number = 600851475143
factor = 2
factor_list = []

num = number
while factor <= num:
    if num % factor == 0:
        factor_list.append(factor)
        num = num // factor
    else: 
        factor += 1

# 2. 소수의 최댓값을 구한다.
# print(factor_list)
print("{}의 소인수 중에서 가장 큰 수는 {}".format(number, max(factor_list)))