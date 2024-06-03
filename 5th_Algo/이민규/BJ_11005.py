input_data = input().split()
num = int(input_data[0])  # 10진수 정수
base = int(input_data[1])  # 변환할 진법
mapping_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
i = 0

while num >= pow(base, i):
    i += 1

temp = 0
while i > 0:
    power = pow(base, i - 1)
    print(mapping_string[num // power], end ='')
    num = num - ((num // power) * power)
    i -= 1
