import sys

def fix_pieces(counts):
    pieces = [1, 1, 2, 2, 2, 8]
    for i in range(len(pieces)):
        print(pieces[i] - counts[i], end=' ')


if __name__ == '__main__':
    counts = list(map(int, sys.stdin.readline().split()))
    fix_pieces(counts)

