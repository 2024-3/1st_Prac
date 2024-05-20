a = list(input())
b = a.copy()

for i in range(len(a)):
    b[i] = a[-i - 1]

if a == b:
    print(1)
else:
    print(0)