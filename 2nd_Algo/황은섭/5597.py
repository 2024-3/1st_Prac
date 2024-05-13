a = [x for x in range(1, 31)]
for i in range(28):
  b = int(input())
  a.remove(b)

for i in range(2):
  print(a[i])