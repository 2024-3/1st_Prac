import sys

def str_repeat(R, S):
    R = int(R)
    for i in range(0, len(S)):
        print(S[i]*R, end='')
    print()


if __name__ == '__main__':
    T = int(sys.stdin.readline().strip())
    for _ in range(T):
        R, S = map(str, sys.stdin.readline().split())
        str_repeat(R, S)