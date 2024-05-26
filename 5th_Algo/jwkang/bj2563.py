import sys

def area_calc(num):
    area = [[0]*100 for _ in range(100)]
    total = 0

    for _ in range(num):
        x, y = map(int, sys.stdin.readline().split())
        for i in range(x, x+10):
            for j in range(y, y+10):
                area[i][j] = 1
 
    for i in range(100):
        total += area[i].count(1)

    print(total)


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    area_calc(N)
    
    