# problem005.py
""" 
1 ~ 10 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 2520입니다.
그러면 1 ~ 20 사이의 어떤 수로도 나누어 떨어지는 가장 작은 수는 얼마입니까? 
"""
i = 1
while True:
    i += 1    
    for j in range(20, 2, -1):
        if i % j != 0:
            break
    if j == 1:
        print(i)
        break
