#p012.py

""" 1부터 n까지의 자연수를 차례로 더하여 구해진 값을 삼각수라고 합니다.
예를 들어 7번째 삼각수는 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28이 됩니다.

그러면 500개 이상의 약수를 갖는 가장 작은 삼각수는 얼마입니까? """

# 약수의 개수 : 소인수분해를 한 후 각 지수에 1을 더한 값을 곱한다.
# 삼각수의 공식 : n(n+1)/2

# [풀이1] 소수들의 지수를 통해 약수의 개수를 구한 후, 약수의 개수를 만족하는 삼각수를 구함
#1. 소인수분해를 통해 약수의 개수를 구하는 함수를 정의
""" def findSquare(num):
    factor = 2
    count = 0   # 지수를 구하기 위한 변수
    primes = []   # 소인수 리스트
    squares = []   # 지수들의 리스트
    while(factor <= num):    
        if num % factor == 0:
            count += 1  
            primes.append(factor)
            num = num // factor
        else:
            if count > 0:
                squares.append(primes.count(factor))
            factor += 1
            count = 0
    squares.append(primes.count(factor))
    # 각 지수에 1을 더한 수를 모두 곱함 : 약수의 개수
    div = 1
    for j in squares:
        div *= (j+1)    
    return(div)

#2. 삼각수와 약수의 개수를 구한다.
MIN = 500           # 500개 이상
triangular = 0      # 삼각수
i = 1               # 반복변수
while True:
    triangular += i
    num_div = findSquare(triangular)
    if num_div >= MIN:
        print(triangular, num_div)
        break
    else: 
        i += 1 """

# [풀이2] 1/2 제곱의 수를 이용하여 약수를 구한 후, 약수의 개수를 만족하는 삼각수를 구함.
# 약수의 개수를 구하는 함수 
# : num이 제곱수이면 제곱근까지의 약수의 개수에 두 배를 한 뒤 1을 빼고, 제곱수가 아니면 제곱근까지의 약수의 개수에 두 배만 한다.
def numDivisors(num):
    number = 0
    #print(num**0.5)
    for i in range(1, int(num**0.5)+1):  # 제곱근까지 약수의 개수를 구함
        if num % i == 0:
            number += 1
    number *= 2
    if int(num**0.5)**2 == num:
        number -= 1
    return number

#삼각수의 공식을 이용하여 약수의 개수를 만족하는 삼각수를 구함
n = 0
while True:
    n += 1
    triangular = int(n*(n+1)/2)     # n번째 삼각수
    if numDivisors(triangular) >= 500:
        print(triangular, n, numDivisors(triangular))
        break

""" # [풀이3] 풀이2 변형
n = 0
triangular = 0
number = 0
while number < 500:
    n += 1
    triangular = n*(n+1)/2
    number = 0
    for i in range(1, int(triangular**0.5)+1):
        if triangular % i == 0:
            number += 1
    number *= 2
    if int(triangular**0.5)**2 == triangular:
        number -= 1
print(triangular, n, number) """














