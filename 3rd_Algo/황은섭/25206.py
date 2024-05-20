dic = {"A+": 4.5,"A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
sum = 0
sub_sum = 0

for _ in range(20):
  sub_input = input().split()
  if sub_input[2] == 'P':
    continue
  else:
    sum += float(sub_input[1]) * dic[sub_input[2]]
    sub_sum += float(sub_input[1])

result = sum / sub_sum
print(result)

