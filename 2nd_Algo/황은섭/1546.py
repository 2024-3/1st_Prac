n = int(input())

grade = []
line = map(int, input().split())
for i in line:
  grade.append(i)

G = [x/max(grade) for x in grade]
print(sum(G)/len(G)*100)
