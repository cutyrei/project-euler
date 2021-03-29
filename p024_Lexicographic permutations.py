#p024.0y
""" 어떤 대상을 순서에 따라 배열한 것을 순열이라고 합니다. 예를 들어 3124는 숫자 1, 2, 3, 4로 만들 수 있는 순열 중 하나입니다.
이렇게 만들 수 있는 모든 순열을 숫자나 문자 순으로 늘어놓은 것을 사전식(lexicographic) 순서라고 합니다.
0, 1, 2로 만들 수 있는 사전식 순열은 다음과 같습니다.
012   021   102   120   201   210

0, 1, 2, 3, 4, 5, 6, 7, 8, 9로 만들 수 있는 사전식 순열에서 1,000,000번째는 무엇입니까? """

import time
import math
start = time.time()

numbers = [0,1,2,3,4,5,6,7,8,9]
result = ""
target_index = 1000000 - 1

for i in range(len(numbers), 0, -1):
    #print("target: ", target_index)
    location = int(target_index / math.factorial(i) * i)
    target_index -= location * math.factorial(i-1)
    #print(i, location, numbers[location])
    result += str(numbers[location])
    numbers.pop(location)
    #print(numbers)
    #print(result)
print(int(result))   


print("time: ", time.time() - start)