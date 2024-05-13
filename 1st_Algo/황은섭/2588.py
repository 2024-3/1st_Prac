a = int(input())
b = str(input())

for i in range(2, -1, -1):
  print(int(b[i]) * a)
print(int(b) * a)