import sys

def count_words(words):
    print(len(words))


if __name__ == '__main__':
    words = sys.stdin.readline().split()
    count_words(words)
    
