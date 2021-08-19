#myFuntions

# 순환소수의 순환마디
print("순환소수의 순환마디 : 순환마디만 출력")
def repeating_decimal(n):
    quotients = ''
    remainders = []
    r = 1
    while r > 0:
        remainders.append(r)
        q, r = divmod(r*10, n)
        quotients += str(q)
        if r in remainders:
            index = remainders.index(r)
            return quotients[index:]
    return

print(repeating_decimal(6))


# 유클리드 호제법 최대 공약수
print("유클리드 호제법 최대공약수 연습")
def gcd(a, b):
    m, n = max(int(a), int(b)), min(int(a), int(b))
    r = m % n
    while r > 0:
        m, n = n, r
        r = m % n
        if r == 0:
            return n

print(gcd(5627, 4403))

# 연분수 변환(유리수)
print("#유리수의 연분수 연습")
def cont_fraction(a, b):
    numer, denom = int(a), int(b)
    result = '[{}; '.format(numer // denom)
    tmp = numer = numer % denom
    numer = denom
    denom = tmp
    while(denom):
        result += f'{numer // denom}, '
        tmp = numer = numer % denom
        numer = denom
        denom = tmp
    result += '\b\b]'
    return result

print(cont_fraction(5627, 4403))

# 무리수의 연분수 전개와 반복 주기
# https://en.wikipedia.org/wiki/Periodic_continued_fraction : Length of the repeating block 의 iterative algorithm
# 일반적인 연분수 확장을 단계별로 적어보면 오른 쪽과 같다 : x0 = √N = a0+1/x1, x1 = a1+1/x2, x2 = a2+1/x3, ... -> xk = (sqrt(N)+mk)/dk
print("#무리수의 연분수 전개와 반복 주기")
def continued_fraction(n):
    a0 = int(n**0.5) # 최초 정수부
    m = 0
    d = 1
    a = a0  # 정수부 값
    t = [] # 정수부 반복 주기
    while a != 2 * a0: # 연분수를 자세히 보면, 정수부가 최초 정수부의 2배가 되는 곳이 주기의 마지막임.
        if a0 ** 2 == n: break
        m = d * a - m
        d = (n - m ** 2) // d        
        a = (a0 + m) // d
        t.append(a)
    print(f'[{a0};{tuple(t)}]', "주기:", len(t))

continued_fraction(7)

