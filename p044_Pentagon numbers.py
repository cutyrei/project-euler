# p044.py
""" 오각수는 Pn = n (3n − 1)/2 라는 공식으로 구할 수 있고, 처음 10개의 오각수는 다음과 같습니다.
1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
위에서 P4 + P7 = 22 + 70 = 92 = P8이 됨을 볼 수 있습니다. 하지만 두 값의 차인 70 − 22 = 48 은 오각수가 아닙니다.
합과 차 모두 오각수인 두 오각수 Pj, Pk 에 대해서, 그 차이 D = | Pk − Pj | 는 가장 작을 때 얼마입니까? """

import time
start = time.time()

# [풀이 1] 오각수를 하나씩 만들어가면서, 오각수 리스트 내 임의의 두 수와 두 수의 차가 오각수 리스트에 존재하는지 확인 : 0.9s(+)
# 집합자료형과 리스트자료형을 같이 생성하여 색인은 집합자료형을 순서는 리스트자료형을 이용

# def is_P(num):    # 오각수를 확인하는 함수1 - 첫째 항 1부터 공차 3인 등차수열로 빼나가서 0이 되면 오각수
#     i = 1; count = 0
#     while (1):
#         num -= i; count += 1        
#         if num == 0: return True
#             #print(count, "번째 오각수"); break
#         elif num < 0: return False
#             #print("오각수 아님"); break
#         else: i += 3

# def is_P_2(n):  # 오각수를 확인하는 함수2
#     import math
#     if math.sqrt(1 + 24*n) % 6 == 5: return True
#     else: return False

# def is_P_3(p): # 오각수를 확인하는 함수3 - n이 자연수이면 오각수(n번째 오각수)
#     n = ((24 * p + 1)**0.5 + 1) / 6
#     return n == int(n)

# def find():
#     p_nums = []
#     s = set(p_nums)
#     n = 1 
#     chk = True
#     while chk:
#         k = int(n*(3*n-1)/2)
#         for i in p_nums:
#             j = k - i
#             d = abs(i - j)
#             if j in s and d in s:
#                 return[p_nums.index(i)+1, i, p_nums.index(j)+1, j, k, d] # 1020번째 오각수 1560090, 2167번째 오각수 7042750, 합 8602840, 차 5482660
#         p_nums.append(k)
#         s.add(k)
#         n += 1

# print(find())









print(time.time()-start)