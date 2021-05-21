# p051.py
""" 두 자리 수 *3의 첫번째 자리를 여러가지로 바꿨을 때 가능한 아홉 가지의 결과 중에서 13, 23, 43, 53, 73, 83의 여섯 개는 소수입니다.
56**3 의 3번째와 4번째 자리를 동일한 숫자로 바꿔서 만들어지는 10개의 다섯자리 수 중에서는 아래에서 보듯이 7개가 소수가 되며, 이것은 이런 식으로 7개의 소수가 만들어지는 첫번째 경우입니다. 
이 소수 집단의 첫번째 수인 56003은 이런 성질을 갖는 가장 작은 소수입니다.
56003, 56113, 56333, 56443, 56663, 56773, 56993
위의 예처럼 원래의 일부를 동일한 숫자로 치환했을 때 8개의 소수 집단이 만들어지는 경우를 찾고, 그 집단에 속한 가장 작은 소수를 구하세요.
치환하는 자리는 인접하지 않아도 되고, 가장 앞부분을 치환하는 경우 거기에 0은 올 수 없습니다. """

import time
start = time.time()

def is_prime(n):    
    if n < 2: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


# [풀이 1] 6자리 수에서 3자리를 변경한다고 생각하고, 둘째~다섯째 자리 안의 수를 바꿔 가면서 억지로 찾았음. 추가 연구 필요.
a = [x for x in range(111111, 1000000) if is_prime(x)]
chk = True
for i in a:
    t = []
    b = str(i)
    for j in range(10):
        c = b.replace(b[1:2], str(j)*3)
        c = b.replace(b[4], str(j))
        if is_prime(int(c)):
            t.append(c)
        if len(t) == 8:
            chk = False
            break
    if chk == False:
        break
print(t)


print(time.time()-start)