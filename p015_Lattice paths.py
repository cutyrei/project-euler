#p015.py
# 2 × 2 격자의 왼쪽 위 모서리에서 출발하여 오른쪽 아래 모서리까지 도달하는 길은 모두 6가지가 있습니다(거슬러 가지는 않기로 합니다).
# 그러면 20 × 20 격자에는 모두 몇 개의 경로가 있습니까?
# r-순열 : P(n, r) 또는 nPr = n!/(n-r)!, 같은 것이 있는 순열 : n = p+q+r 일 때, n!/(p!*q!*r!)

import time
start = time.time()

grid = 20

a = 1
for i in range(1, grid+1):
    a *= i

b = 1
for j in range(1, (grid+grid)+1):
    b *= j

print(int(b / (a*a)))

print("runnig time: ", time.time() - start)
