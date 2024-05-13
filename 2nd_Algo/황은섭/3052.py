S = set()
for i in range(10):
  a = int(input())
  S.add(a%42)
print(len(S))