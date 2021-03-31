#p028.py
""" 수 1부터 시작해서 우측으로부터 시계방향으로 감아 5×5 행렬을 만들면 아래와 같이 됩니다.
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
여기서 대각선 상의 수를 모두 더한 값은 101 입니다.

같은 방식으로 1001×1001 행렬을 만들었을 때, 대각선 상의 수를 더하면 얼마가 됩니까? """

import time
start = time.time()

# [풀이1] 각 대각선 방향별로 수열 규칙(이전 2개 항의 차에 8을 더한 수 만큼 증가)에 따른 합을 구한 뒤, 전체 합을 구하는 방법
# MAX = 1001
# def diagonals(a):
#     nums = [1, a] + [0]*(int(MAX/2)-1)
#     for i in range(2, len(nums)):
#         nums[i] = nums[i-1] + (nums[i-1]-nums[i-2]+8)
#     return sum(nums[1:])

# print(1+diagonals(3)+diagonals(5)+diagonals(7)+diagonals(9))

# [풀이2] 1 이후, 1회 회전할 때마다 2의 배수 만큼 증가하는 4개의 수를 찾는 것을 500 회 증가하는 방법
# MAX = 1001
# number = 1
# result = 1
# for i in range(1, int(MAX/2)+1):
#     for j in range(4):
#         number += 2*i
#         result += number
#         #print(number, result)
# print(result)

# [풀이3] N*N 배열에서 대각선 원소들의 합 : N = 2*n + 1 일 때, 2/3*n*(8*(n**2)+15*n+13)+1
# 참고링크 : https://blog.naver.com/kyh941031/221679263232
N = 1001
n = (N-1)/2
print(2/3*n*(8*(n**2)+15*n+13)+1)


print("time: ", time.time()-start)

