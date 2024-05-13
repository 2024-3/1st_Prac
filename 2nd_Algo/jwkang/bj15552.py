import sys

def fast_add(n):
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        print(a + b)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    fast_add(n)




