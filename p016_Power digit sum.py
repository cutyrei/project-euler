#p016.py
""" 2^15 = 32768 의 각 자릿수를 더하면 3 + 2 + 7 + 6 + 8 = 26 입니다.
2^1000의 각 자릿수를 모두 더하면 얼마입니까? """

import time
start = time.time()

a = str(2**1000)
#result = 0
# for i in a:
#     result += int(i)

result = sum(map(int, a))
print(result)

print("running time: ", time.time() - start)
