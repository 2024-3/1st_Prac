import sys

while True:
    line = sys.stdin.readline().rstrip()
    if not line:
        break
    A, B = map(int, line.split())
    print(A + B)
