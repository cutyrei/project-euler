#p019.py
""" You are given the following information, but you may prefer to do some research for yourself.
1 Jan 1900 was a Monday.
Thirty days has September, April, June and November.
All the rest have thirty-one, Saving February alone, Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)? """
# 1900년 1월 1일은 월요일. 400으로 나누어 떨어지는 매100년은 윤년 -> 2000년은 윤년, 2000년부터 4년씩 감소하는 해가 윤년, 단 1900년은 윤년 아님(100년 주기는 윤년 아님). 
# 매월 1일이 일요일 => 20세기(1901~2000)에서 일요일로 시작하는 월의 개수는?

import time
start = time.time()

# # [풀이1] 
# leap_year = []    # 윤년인 해를 저장
# for i in range(2000, 1899, -4):
#     if i % 400 == 0 or i % 100 != 0:
#         leap_year.append(i)

# days = [31,28,31,30,31,30,31,31,30,31,30,31]    # 월별 일수(1~12월)
# date = 1                                            # 시작 요일 변수(일요일-토요일 : 0,1,2,3,4,5,6)  *1900년 1월 1일은 월요일.
# month = 1                                           # 시작 월 변수
# sundays = []                                        # 1900년-2000년까지 연도별 일요일로 시작하는 월의 개수를 리스트로 저장

# for y in range(1900, 2001):                         # 연도를 센다.
#     if y in leap_year:                              # 윤년인지 확인한다.
#         days[1] = 29        
#     else:
#         days[1] = 28
#     count = 0                                       # 일요일로 시작하는 월의 개수를 저장하는 변수
#     for day in days:                                # 월을 센다.
#         if date == 0:                               # 월의 시작이 일요일인 경우를 센다
#             count += 1
#             # if y > 1900: # echo
#             #     print(y, "년 ", month, "월")
#         for i in range(day):                        # 날짜별 요일을 계산한다.  
#             date += 1
#             if date > 6: date = 0
#         # month += 1
#         # if month > 12: month = 1
#     sundays.append(count)
# print(sum(sundays[1:]))                             # 일요일로 시작하는 월의 개수의 합을 출력한다(1900년은 제외-sundays[0]).



# [풀이2]
days = [31,28,31,30,31,30,31,31,30,31,30,31]
date = 0    # 1900-01-01 월요일
count = 0

for y in range(1900, 2001):
    for m in range(12):   
        day = days[m]   
        if y % 4 == 0 and m == 1:
            day += 1      
        for d in range(day):
            # if date % 7 == 6: # 월요일-일요일 : 0-6
            #     print(y, m+1, d+1)
            if y > 1900 and d == 0 and date % 7 == 6:
                count += 1
            date += 1
print(count)


print(time.time()-start)