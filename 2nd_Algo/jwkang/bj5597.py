import sys

def hw_check():
    list = [_ for _ in range(1, 31)]
    for _ in range(28):
        list.remove(int(sys.stdin.readline().strip()))
    list.sort()
    print(f'{list[0]}\n{list[1]}')


if __name__ == '__main__':
    hw_check()



