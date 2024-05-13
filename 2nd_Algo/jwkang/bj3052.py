import sys

def remain_comp():
    remain = set([])
    for _ in range(10):
        remain.add(int(sys.stdin.readline().strip()) % 42)
    print(len(remain))


if __name__ == '__main__':
    remain_comp()


