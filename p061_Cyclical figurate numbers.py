# p061.py
""" 삼각수, 사각수, 오각수 같은 다각수들은 아래의 공식으로 만들 수 있습니다.
삼각수	P3,n = n(n+1)/2	    1, 3, 6, 10, 15, ...
사각수	P4,n = n2	        1, 4, 9, 16, 25, ...
오각수	P5,n = n(3n−1)/2	1, 5, 12, 22, 35, ...
육각수	P6,n = n(2n−1)	    1, 6, 15, 28, 45, ...
칠각수	P7,n = n(5n−3)/2	1, 7, 18, 34, 55, ...
팔각수	P8,n = n(3n−2)	    1, 8, 21, 40, 65, ...
그런데 4자리 수 8128, 2882, 8281 (순서대로) 에는 세 가지의 재미있는 성질이 있습니다.
각 수는 서로 꼬리를 물고 순환됩니다. 각 수의 뒤쪽 두 자리는 다음 수의 앞쪽 두 자리가 되는 식입니다.
각 수는 서로 다른 다각수인데, 여기서는 삼각수 (P3,127=8128), 사각수 (P4,91=8281), 오각수 (P5,44=2882)가 대응됩니다.
이런 성질을 갖는 4자리의 수 세 개는 이 수들이 유일합니다.
위와 같이 순환되면서 서로 다른 다각수(삼각수 ~ 팔각수)이기도 한 4자리 수 여섯 개의 유일한 순서쌍을 찾고, 그 합을 구하세요. """

import time
start = time.time()

# # [풀이 1] 서로 중복되지 않는 4자리 다각수 집합을 만든 후, 그 수 안에서 순환되는 6개의 수를 골라 다각수 여부를 확인 : 10s 이상
# # 순서쌍을 찾는 부분에서 10초 이상 소요됨.
#
# print("=== start ===")
#
# # 삼각수~팔각수 판별 함수(근의공식으로 변환)
# def is_tri(x): n = (pow(8*x+1, 0.5)-1)/2; return n == int(n)
# def is_square(x): n = pow(4*x, 0.5)/2; return n == int(n)
# def is_penta(x): n = (pow(24*x+1, 0.5)+1)/6; return n == int(n)
# def is_hex(x): n = (pow(8*x+1, 0.5)+1)/4; return n == int(n)
# def is_hep(x): n = (pow(40*x+9, 0.5)+3)/10; return n == int(n)
# def is_oct(x): n = (pow(12*x+4, 0.5)+2)/6; return n == int(n)
#
# print("# 리스트 생성 시작 : ", time.time()-start)
#
# # 네 자리 숫자들 중 서로 중복되는 숫자가 없는 삼각수~팔각수 리스트 만들기
# # 육각수는 삼각수에 포함되는 등 2개 이상의 다각수에 해당하는 수의 경우에는 가장 큰 다각수로 판정 
# tri = set()
# square = set()
# penta = set()
# hexa = set()
# hep = set()
# octa = set()
#
# for i in range(1001, 10000):
#     if is_oct(i): octa.add(i); continue
#     elif is_hep(i): hep.add(i); continue
#     elif is_hex(i): hexa.add(i); continue
#     elif is_penta(i): penta.add(i); continue
#     elif is_square(i): square.add(i); continue
#     elif is_tri(i): tri.add(i)
#
# all_nums = tri | square | penta | hexa | hep | octa
#
# print("# 리스트 생성 완료 : ", time.time()-start)
# print("# 순서쌍 찾기 시작 : ", time.time()-start)
#
# # 순환되는 순서쌍 리스트
# p_nums = []
# for a in all_nums:
#     for b in all_nums:
#         if b == a or str(b)[:2] != str(a)[2:]: continue
#         for c in all_nums:
#             if c == a or c == b or str(c)[:2] != str(b)[2:]: continue
#             for d in all_nums:
#                 if d == a or d == b or d == c or str(d)[:2] != str(c)[2:]: continue
#                 for e in all_nums:
#                     if e == a or e == b or e == c or e == d or str(e)[:2] != str(d)[2:]: continue
#                     for f in all_nums:
#                         if f == a or f == b or f == c or f == d or f == e or str(f)[:2] != str(e)[2:]: continue
#                         if str(f)[2:] == str(a)[:2]:
#                             p_nums.append([a, b, c, d, e, f])
#
# print("# 순서쌍 찾기 완료 : ", time.time()-start)
#
# print("# 조건 수 찾기 시작 : ", time.time()-start)
#
# def what(i):
#     if i in octa: return 8
#     elif i in hep: return 7
#     elif i in hexa: return 6
#     elif i in penta: return 5
#     elif i in square: return 4
#     elif i in tri: return 3
#     else: return 'n'
#
# for i in p_nums:
#     code = []
#     for j in i:
#         code.append(what(j))
#     chk = ''.join(sorted(list(map(str, code))))
#     if chk == '345678':
#         print(i, code, sum(i))
#
# print("# 조건 수 찾기 완료 : ", time.time()-start)

###############################################################################

# [풀이 2] https://soooprmx.com/%EC%98%A4%EC%9D%BC%EB%9F%AC-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-61/ : 0.4s
# 각 다각수별로 200항까지의 수를 구한 후(make_numbers()), 그 중 4자리인 숫자들만 모은 다음(numbers - (N각수, 숫자)의 리스트), 각 수의 뒤 2자리와 순환하는 수들을 찾음(links)
# 순환 판별 : 4자리 수이므로, 그 수를 100으로 나누었을 때의 몫이 앞의 2자리이고 나머지가 뒤의 2자리가 됨.

def make_numbers(n):
    return [n*(n+1)//2, n*n, n*(3*n-1)//2, n*(2*n-1), n*(5*n-3)//2, n*(3*n-2)]

numbers = []
for n in range(1, 200):
    for i, m in enumerate(make_numbers(n)):
        if 1000 <= m < 10000:
            numbers.append((i+3, m))

links = dict()
for x in numbers:
    links[x] = [y for y in numbers if y[0] != x[0] and x[1] % 100 == y[1] // 100] # 동일한 다각수가 아니면서 순환 조건에 해당하는 수들을 찾음

def test(node, level, acc):
    if level is 0:
        if acc[-1][1] % 100 == acc[0][1] // 100:
            return acc
        return None
    ## 현재 노드에서 연결될 수 있는 노드 중에서, 누적 링크와 같은 다각수는 제외하고 체크
    for c in [x for x in links[node] if x[0] not in [y[0] for y in acc]]:
        new_acc = acc + [c]
        result = test(c, level - 1, new_acc)
        if result:
            return result
        return None

for n in numbers:
    result = test(n, 6, [])
    if result:        
        print(sum(x[1] for x in result), result)
        break



print(time.time()-start)