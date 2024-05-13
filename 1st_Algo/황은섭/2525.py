A, B = map(int, input().split())
C = int(input())

a, B = divmod(B+C, 60)
print((A+a)%24, B)