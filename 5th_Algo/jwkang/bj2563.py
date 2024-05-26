import sys

def area_calc(num):
    base = [[0]*100 for _ in range(100)]
    area = 0

    for _ in range(num):
        x, y = map(int, sys.stdin.readline().split())
        for i in range(x, x+10):
            for j in range(y, y+10):
                base[i][j] = 1
 
    for i in range(100):
        area += base[i].count(1)

    print(area)


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    area_calc(N)
    
    