import string

a = str(input()).upper()
a_count = []

for letter in string.ascii_uppercase:
    a_count.append(a.count(letter))  # letter 별로 몇 개씩 있는지 확인

a_max = max(a_count)  # 제일 숫자가 많은 놈이 몇 개인지 확인.
count_max = a_count.count(a_max)  # 제일 큰 숫자의 갯수 확인

if count_max >= 2:  # 2개 이상이면 ?출력
    print("?")
else:
    a_max_index = a_count.index(a_max)  # 제일 큰 놈 인덱스 알아내기
    print(string.ascii_uppercase[a_max_index])  # 1개면 대문자로 해당 문자 출력

