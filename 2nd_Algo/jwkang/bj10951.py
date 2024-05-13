import sys

def add():
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)


if __name__ == '__main__':
    while True:
        try:
            add()
        except:
            break



