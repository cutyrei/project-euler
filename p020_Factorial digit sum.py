#p020.py
""" n! 이라는 표기법은 n × (n − 1) × ... × 3 × 2 × 1을 뜻합니다.
예를 들자면 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 이 되는데,
여기서 10!의 각 자릿수를 더해 보면 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 입니다.
100! 의 자릿수를 모두 더하면 얼마입니까? """

#1. 100!를 구한다.
a = 1
for i in range(1, 101):
    a *= i
# 2. 1에서 나온 값의 각 자리 수의 합을 구한다.
# b = str(a)
# result = 0
# for j in b:
#     result += int(j)
# 3. 합을 출력한다.
# print(result)

#print([sum(int(j) for j in str(a))][0])
print(sum(map(int, str(a))))

################

# #[풀이2] math 모듈을 사용하고, 한 줄 식으로 표시
# import math
# #print([sum(int(i) for i in str(math.factorial(100)))][0])
# print(sum(map(int, str(math.factorial(100)))))

# #[풀이3] 또 다른 간단한 식 : 모듈을 식에 삽입 __import__('모듈명')
# print(__import__('functools').reduce(lambda x, y: int(x) + int(y), str(__import__('math').factorial(100))))