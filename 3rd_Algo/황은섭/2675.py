T = int(input())

for i in range(T):
  S, R = input().split()
  S = int(S)

  for j in R:
    print(j*S, end ='')
  print()