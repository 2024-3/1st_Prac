import sys

def print_star(N):
    for i in range(1, N):
        print(' '*(N-i) + '*'*(2*i-1))

    for i in range(N, 0, -1):
        print(' '*(N-i) + '*'*(2*i-1))


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    print_star(N)

