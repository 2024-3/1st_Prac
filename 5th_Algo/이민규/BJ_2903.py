try_num = 0;
temp = 2;
try_num = int(input())
while try_num > 0:
    temp += (temp - 1);
    try_num -= 1;
    
print(temp * temp);
