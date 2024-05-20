import sys

def set_alarm(h, m):
    if m < 45:
        m += 15
        h = (h - 1) % 24
    else:
        m -= 45

    return f'{h} {m}'

if __name__ == '__main__':
    h, m = map(int, sys.stdin.readline().split())
    print(set_alarm(h, m))




