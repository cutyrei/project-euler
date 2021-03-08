# problem004.py
""" 
앞에서부터 읽을 때나 뒤에서부터 읽을 때나 모양이 같은 수를 대칭수(palindrome)라고 부릅니다.
두 자리 수를 곱해 만들 수 있는 대칭수 중 가장 큰 수는 9009 (= 91 × 99) 입니다.
세 자리 수를 곱해 만들 수 있는 가장 큰 대칭수는 얼마입니까? 
"""
# 1. 세 자리 수를 곱한다.
palindrome = []
for i in range(100, 1000):
    for j in range(100, 1000):
        k = str(i * j)
        # 2. 대칭수를 찾는다(k의 각 인덱스 값을 비교).
        # for n in range(len(k)):
        #     if k[n] != k[-(n+1)]: 
        #         break
        # else:
        #     palindrome.append(int(k))
        #     #print(i, j, k)
        if k == k[::-1] :   # 2. 대칭수를 찾는다 : 인덱스를 뒤집은 것과 같은지 비교
            palindrome.append(int(k))

# 3. 대칭수 중 가장 큰 수를 출력한다.
print(max(palindrome))

# 리스트내포 방법으로 간략히 처리(가장 큰 수이므로, 900 이상 숫자들을 곱해서 최대값 찾기)
print(max([i * j for i in range(999,900,-1) for j in range(999,900,-1) if str(i*j) == str(i*j)[::-1]]))
