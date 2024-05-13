import sys

def isgroupword(word):
    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            continue
        elif word[i] in word[i+1:]:
            return 1
    return 0


if __name__ == '__main__':
    N = int(sys.stdin.readline().strip())
    for _ in range(N):
        word = str(sys.stdin.readline().strip().upper())
        N -= isgroupword(word)
    print(N)

