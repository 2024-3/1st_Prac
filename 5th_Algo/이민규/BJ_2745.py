input_data = input().split()
string = input_data[0]
base = int(input_data[1])
temp = 0
result = 0

for i in range(len(string)):
    c = string[i]
    if c >= 'A' and c <= 'Z':
        temp = ord(c) - ord('A') + 10
    else:
        temp = ord(c) - ord('0')
    
    result = result + temp * pow(base, len(string) - i - 1)
    
print(result)
