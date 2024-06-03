import sys

def calc_terrain(N):
    print(((2**N)+1)**2)


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    calc_terrain(N)


