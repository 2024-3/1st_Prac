import sys

def number_conv(N, B):
    print(int(N, int(B)))


if __name__ == '__main__':
    N, B = map(str, sys.stdin.readline().split())
    number_conv(N, B)



