paper_num = int(input())
field = [[0] * 100 for _ in range(100)]

for i in range(paper_num):
    low_x_pos, low_y_pos = map(int, input().split())
    for x in range(low_x_pos, low_x_pos + 10):
        for y in range(low_y_pos, low_y_pos + 10):
            field[x][y] = 1

area = 0
for x in range(100):
    area += field[x].count(1)

print(area)
