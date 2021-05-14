# p048.py
""" 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317 입니다.
1^1 + 2^2 + 3^3 + ... + 1000^1000 의 마지막 10자리 수는 무엇입니까? """
import time
start = time.time()

# [풀이 1] 그냥 제곱해서 더한 후, 마지막 10자리 출력 : 0.009s(-)
sum = 0
for i in range(1, 1001):
    sum += i**i
print(str(sum)[-10:])
# # print(str(sum(i**i for i in range(1, 1001)))[-10:]) # 리스트 컴프리헨션 0.01s(+) vs. 위 풀어쓴 식 0.009s(-)



print(time.time()-start)