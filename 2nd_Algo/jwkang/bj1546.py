import sys

def fix_score(n):
    scores = list(map(int, sys.stdin.readline().split()))
    M = max(scores)
    corrects = [score/M * 100 for score in scores]
    mean = sum(corrects) / n
    print(mean)


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    fix_score(n)



