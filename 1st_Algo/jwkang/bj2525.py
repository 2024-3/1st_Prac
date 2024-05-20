from datetime import datetime, timedelta
import sys

def cook_timer(h, m, n):
    current_time = datetime(year=1, month=1, day=1, hour=h, minute=m)
    new_time = current_time + timedelta(minutes=n)
    return f'{new_time.hour} {new_time.minute}'

if __name__ == '__main__':
    h, m = map(int, sys.stdin.readline().split())
    n = int(sys.stdin.readline().strip())
    
    print(cook_timer(h, m, n))





    