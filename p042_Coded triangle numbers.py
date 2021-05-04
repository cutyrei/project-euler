# p042.py
""" n번째 삼각수는 t(n) = ½ * n*(n + 1) 이라는 식으로 구할 수 있는데, 처음 10개는 아래와 같습니다.
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
어떤 영어 단어에 대해서, 각 철자의 알파벳 순서(A=1, B=2, ..., Z=26)를 모두 더한 값을 '단어값'이라 부르기로 합니다. 예를 들어 'SKY'의 단어값은 19 + 11 + 25 = 55가 되는데, 이것은 우연히도 t10과 같습니다.
이렇게 어떤 단어의 단어값이 삼각수일 경우에는 이 단어를 '삼각단어'라 부르기로 합니다.
약 16KB의 텍스트 파일 words.txt에는 2000개 정도의 영어 단어가 수록되어 있습니다. 이 중에서 삼각단어는 모두 몇 개입니까? """
import time
start = time.time()

# 파일의 내용을 리스트로 만든다.
f = open("p042_words.txt", 'r')
words = f.read().replace('"','').split(',')
f.close()
words.sort()
#values = 'abcdefghijklmnopqrstuvwxyz'.upper()

# [풀이1] 파일의 가장 긴 단어로 삼각수 리스트 길이의 최댓값을 정한 뒤, 삼각단어를 찾기 : 0.009s(+)
# m = 0
# for i in words:
#     if m < len(i):
#         m = len(i)
#         p = i
# print(m, p) # 가장 긴 단어(긴 자릿수=m) ADMINISTRATION(=p) - 14 * 26(z의 수) = 364 -> 364 이하의 삼각수

tri_nums = [0]
i = 1
while True:
    n = int(i*(i+1) / 2)
    if n > 364: break
    tri_nums.append(n)
    i += 1
print(tri_nums)

count = 0
for i in range(len(words)):
    sum = 0
    for j in words[i]:
        #sum += values.index(j)+1
        sum += ord(j)-64 # 단어값을 위 values의 인덱스를 이용하지 않고, 해당 문자의 아스키 값을 활용해서 바로 계산하는 방법('A'=65)
    if sum in tri_nums:
        count += 1
print(count)


#[풀이2] 삼각수를 확인하는 방법 - 해당 수에서 1부터 1씩 증가한 값을 반복해서 뺄 때 0이 되는 수(삼각수의 모양을 생각) : 0.011s(+)

# def is_tri_num(n):
#     i = 1
#     while n > 0:
#         n -= i
#         i += 1
#     if n == 0: return True
#     return False

# count = 0
# for i in range(len(words)):
#     sum = 0
#     for j in words[i]:
#         sum += values.index(j)+1
#     if is_tri_num(sum):
#         count += 1
# print(count)


# # [풀이3] 한 줄로 축약 : 0.005s(+)
# tri_numbers = [n*(n+1)/2 for n in range(1, 30)]     # 임의의 범위
# print(len([word for word in words if sum([ord(w)-64 for w in word.strip('"')]) in tri_numbers]))


print(time.time()-start)