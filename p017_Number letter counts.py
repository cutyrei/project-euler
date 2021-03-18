#p017.py
""" 1부터 5까지의 수를 영어로 쓰면 one, two, three, four, five 이고,
각 단어의 길이를 더하면 3 + 3 + 5 + 4 + 4 = 19 이므로 사용된 글자는 모두 19개입니다.

1부터 1,000까지 영어로 썼을 때는 모두 몇 개의 글자를 사용해야 할까요?
참고: 빈 칸이나 하이픈('-')은 셈에서 제외하며, 단어 사이의 and 는 셈에 넣습니다.
     예를 들어 342를 영어로 쓰면 three hundred and forty-two 가 되어서 23 글자,
     115 = one hundred and fifteen 의 경우에는 20 글자가 됩니다. """

# 1부터 1000까지의 문자를 리스트에 채워 넣고, 리스트의 길이를 구한다.
# 반복되지 않는 수와 반복해서 사용될 수를 미리 리스트에 넣어 두고, 수를 생설할 때 사용하도록 한다.
# 분류 기준 : 1~9는 계속 사용, 11~19는 한 번만 사용, 10-20-30-...-90->10의 배수들, 100-200-...-800-900->100의 배수들
# 표기시 주의사항 : one hundred, one thousand, 백 단위 세 자리 수를 표시할 때는 'hundred and' 표시

result = 0      
# 리스트 num에 1~19를 기본으로 넣어 두고 20 이후의 수를 추가, num과 tens의 원소들을 재사용해서 반복문으로 수를 만들어 추가 시킨다.
num = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'] 
tens = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

# 20~99 추가
for ten in tens:
    num.append(ten)
    for i in range(9):
        num.append(ten + num[i])

# 100~999 추가
for i in range(9):
    num.append(num[i] + "hundred")
    for j in range(99):
        num.append(num[i] + "hundredand" + num[j])

# 1000 추가
num.append("onethousand")

# 글자 수 세기
for n in num:
    result += int(len(n))

print(result)

