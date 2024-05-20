import sys

def find_type():
    print(int(sys.stdin.readline().strip())//4 * 'long ' + 'int')


if __name__ == '__main__':
    find_type()


