import sys

def add_3(n1, n2, n3):
    return n1 + n2 + n3

if __name__ == '__main__':
    n1, n2, n3 = map(int, sys.stdin.readline().split())
    print(add_3(n1, n2, n3))





    