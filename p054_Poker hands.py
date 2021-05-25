# p054.py
""" 포커라는 카드게임은 다섯 장으로 된 패의 높고 낮음에 따라 승부를 냅니다(포커 규칙을 이미 아는 분이라면 규칙 설명 부분은 건너뛰셔도 좋습니다).
카드 한 장은 아래와 같은 순서대로 값이 높아집니다.
2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A
다섯 장으로 이루어진 패의 계급(세칭 "족보")은, 낮은 것부터 높은 순서로 아래와 같습니다.
High Card : 가장 높은 카드의 값으로 비교.
One Pair : 한 쌍이 같은 카드.
Two Pairs : 서로 다른 두 쌍이 같은 카드.
Three of a Kind : 세 장이 같은 카드.
Straight : 모든 카드가 연속된 숫자.
Flush : 모든 카드의 무늬가 같음.
Full House : 세 장이 같고, 또 한 쌍이 같음 (Three of a Kind + One Pair).
Four of a Kind : 네 장이 같은 카드.
Straight Flush : 모든 카드가 연속된 숫자이면서 무늬도 같음.
Royal Flush : 10, J, Q, K, A가 무늬도 같음.
두 사람의 패가 같은 종류의 계급이라면, 계급을 구성하는 카드 중 높은 쪽을 쥔 사람이 이깁니다. 예를 들면 8 원페어는 5 원페어를 이깁니다.
계급을 이루는 카드 숫자까지 같으면 (예: 둘 다 Q 원페어), 다른 카드를 높은 순서대로 비교해서 승부를 정합니다.

텍스트파일 poker.txt 에는 두 선수가 벌인 1,000회의 승부가 저장되어 있습니다. (우클릭해서 다운로드 받으세요)
한 줄에는 10장의 카드가 공백으로 분리되어 들어있는데, 앞의 다섯 장은 1번 선수 것이고 뒤의 다섯 장은 2번 선수의 패입니다. 잘못되거나 중복된 데이터는 없으며, 무승부도 없습니다.
카드 숫자는 2, 3, ... , 9, T, J, Q, K, A 로 (숫자 10은 T로 표시),
무늬는 C (Club - ♣), D (Diamond - ♦), H (Heart - ♥), S (Spade - ♠) 로 표시되어 있습니다.
예를 들면 3C 3D 3S 9S 9D 의 경우 3 풀하우스가 됩니다.
이 데이터를 분석하고, 1번 선수가 이긴 횟수를 구하세요. """

import time
start = time.time()

# [풀이 1] 카드 정보와 계급 분석 결과를 문자열로 변환 후 비교, 계급이 같은 경우 숫자가 큰 카드가 승리
# (1) 카드 정보 카운트 : 5개 카드 정보를 문자열로 변경 후 숫자 및 무늬를 카운트한 문자열 출력('4H5D5H5S4S' -> 000230000000000122)
def count(card):
    data = '00'
    for i in '23456789TJQKACDHS':   # 2~A : 숫자, CDHS : 무늬(클로버-다이아몬드-하트-스페이드)
        data += str(card.count(i))
    return data

# (2) 카드 해석 : 결과가 같을 경우, (3)에서 가장 큰 수를 추가로 비교 : 0.05s(-)
# def judge(data):
#     result = [0]*9
#     # [1] Royal Flush, [2] Straight Flush, [3] Four of a Kind, [4] Full House, [5] Flush, [6] Straight, [7] Three of a Kind, [8] Two Pairs, [9] One Pair
#     if '11111' in data[10:15] and '5' in data[15:19]:
#         result[0] = 1
#     elif '11111' in data[:14] and '5' in data[15:19]:
#         result[1] = data.rindex('1') # 마지막 수로 크기 비교
#     elif '4' in data[:15]:
#         result[2] = data.index('4')
#     elif '3' in data[:15] and '2' in data[:15]:
#         result[3] = data.index('3')
#     elif '5' in data[15:19]:
#         result[4] = data.index('5')
#     elif '11111' in data[:15]:
#         result[5] = data.rindex('1')
#     elif '3' in data[:15]:
#         result[6] = data.index('3')
#     elif data[:15].count('2') == 2:
#         result[7] = data[:15].rindex('2')  # 마지막 인덱스 값 리턴
#     elif data[:15].count('2') == 1:
#         result[8] = data.index('2')
#     return result

# (2) 카드 해석 방법 개선 - 아래 (3) 생략 가능 : 0.03s(-)
def judge(data):
    nums = data[:15]
    symbols = data[15:]
    result = [0]*9
    if '1' in nums:    result[8] = nums.rindex('1')
    if nums.count('2') == 1:   result[7] = nums.index('2')
    if nums.count('2') == 2:   result[6] = nums.rindex('2')
    if '3' in nums:    result[5] = nums.index('3')
    if '11111' in nums:    result[4] = result[8] #nums.rindex('1')
    if '5' in symbols:    result[3] = result[8] #nums.rindex('1')
    if result[5] != 0 and result[7] != 0: result[2] = result[5]
    if '4' in nums:    result[1] = nums.index('4')
    if result[3] != 0 and result[4] != 0: result[0] = result[4] # 마지막 카드 수로 구별 가능
    return result

with open('p054_poker.txt') as games:
    cards = [''.join(i.split()) for i in games.readlines()]

win = 0
for card in cards:
    if judge(count(card[:10])) > judge(count(card[10:])):
        win += 1
    # (3) judge 값이 같은 경우 가장 큰 수가 있는 쪽이 승리
    # elif judge(count(card[:10])) == judge(count(card[10:])):    
    #     if count(card[:10])[:15][::-1] > count(card[10:])[:15][::-1]:
    #         win += 1
print(win)


print(time.time()-start)