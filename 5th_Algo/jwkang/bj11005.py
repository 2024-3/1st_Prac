import sys

def number_conv(N, B):
    table = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    conv = ''

    while N:
        conv += table[N%B]
        N = N//B

    print(conv[::-1])


if __name__ == '__main__':
    N, B = map(int, sys.stdin.readline().split())
    number_conv(N, B)


    