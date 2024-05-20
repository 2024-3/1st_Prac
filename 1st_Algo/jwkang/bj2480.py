import sys

def winning_calc(n1, n2, n3):
    if [n1, n2, n3].count(n2) == 1:
        win = n3
    elif [n1, n2, n3].count(n2) == 2:
        win = n2 + 10
    else:
        win = n3 * 10 + 100

    return win * 100

if __name__ == '__main__':
    n1, n2, n3 = sorted(map(int, sys.stdin.readline().split()))
    print(winning_calc(n1, n2, n3))




